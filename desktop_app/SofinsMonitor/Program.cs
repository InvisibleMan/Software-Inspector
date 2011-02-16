using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using SofinsCommon;
using System.IO;

namespace SofinsMonitor
{
    class Program
    {
      /// <summary>
      /// state of the pc before current launch of the program
      /// </summary>
      public static SofinsDS previousState;

      /// <summary>
      /// state of the pc during current launch of the program
      /// </summary>
      public static SofinsDS currentState;

      /// <summary>
      /// List of programs that must be excluded from processing
      /// </summary>
      public static SofinsDS blacklist;


      public static string appDataFolder;

      public static string currentStateSavedTo = null;

        static void Main(string[] args)
        {
          //init datasets for later use 
          previousState = new SofinsDS();
          currentState = new SofinsDS();

          appDataFolder = Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData);
          appDataFolder = Path.Combine(appDataFolder, "Sofins"); //yes, a magic string here


          //check if it's time to scan program list
          DateTime dateOfNextCheck =
          Properties.Settings.Default.lastLaunchTime.Add(Properties.Settings.Default.reportPeriod);

          if (DateTime.Now < dateOfNextCheck && System.Environment.MachineName.ToLower() != "homestation")
          {
            return;
          }
          else
            {
              //read the last saved list and compare it to the current list of programs
              if (previousState.LoadFromAppDataFolder(new DirectoryInfo(Program.appDataFolder), null) == false)
              {   //maybe it's the first run of the program, nothing to load
                currentState.PopulateFromRegistry();
                currentStateSavedTo = currentState.SaveToAppDataFolder(new DirectoryInfo(Program.appDataFolder));
                return;
              }
              else
              {
                //everything's OK
                currentState.PopulateFromRegistry();

                //init software blacklist
                blacklist = new SofinsDS();
                string blacklist_filename = Path.Combine(Directory.GetCurrentDirectory(), "program_blacklist.xml");
                blacklist.LoadFromAppDataFolder(null, new FileInfo(blacklist_filename));

                //mark programs that shouldn't be processed
                foreach (SofinsDS.InstalledSoftwareRow inso in currentState.InstalledSoftware )
                  if (-1 != blacklist.IndexOf(inso.sName ))
                    inso.bHidden = true;

                currentStateSavedTo = currentState.SaveToAppDataFolder(new DirectoryInfo(Program.appDataFolder));

                for (int counter = currentState.InstalledSoftware.Count-1; counter > 0; --counter)
                  if (currentState.InstalledSoftware[counter].bHidden == true)
                    currentState.InstalledSoftware.RemoveInstalledSoftwareRow(currentState.InstalledSoftware[counter]);

                currentStateSavedTo = currentState.SaveToAppDataFolder(new DirectoryInfo(Program.appDataFolder));

                //foreach (SofinsDS.InstalledSoftwareRow isr in currentState.InstalledSoftware)
                //{
                //  if (previousState.IndexOf(isr.sName) == -1)
                //    //TODO: a new program found, need to post information about this change to the server
                //    break;
                //}

                bool result = SofinsCommon.SofinsCommon.PostXMLFileToSite(new FileInfo(currentStateSavedTo));

              }

            //update lastLaunchTime variable
            Properties.Settings.Default.lastLaunchTime = DateTime.Now;
            Properties.Settings.Default.Save();
          }
        }
    }
}
