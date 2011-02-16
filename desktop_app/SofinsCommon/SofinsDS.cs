using System;
using System.IO;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Text;
using Microsoft.Win32;

namespace SofinsCommon
{   
    
    public partial class SofinsDS {

        /// <summary>
        /// Saves dataset to the application folder
        /// </summary>
        /// <returns>full path of the file, null if an error occured</returns>
        public string SaveToAppDataFolder(DirectoryInfo di)
        {
            //DirectoryInfo di = new DirectoryInfo(Program.appDataFolder);

            try
            {
                if (!di.Exists)
                    di.Create(); //TODO Error handling!


                string generatedFileName = "programlist_" + DateTime.Today.ToShortDateString() + 
                     "_" +DateTime.Now.ToLongTimeString().Replace(":", "") + ".xml";
                generatedFileName = Path.Combine(di.FullName, generatedFileName);
                this.WriteXml(generatedFileName); //TODO error handling!
                return generatedFileName;
            }
            catch (Exception ex)
            {
                //TODO add logging
                return null;
            }

        }


        /// <summary>
        /// Reads dataset from an XML file
        /// <param name="di">Directory containing the dataset</param>
        /// <param name="fi">File name, if exists. Pass null to load the most recent one</param>
        /// <returns>true is everything's ok, false if there was an error</returns>
        /// </summary>
        public bool LoadFromAppDataFolder(DirectoryInfo di, FileInfo fi)
        {
            //DirectoryInfo di = new DirectoryInfo(Program.appDataFolder);

            try
            {
                if (!di.Exists)
                    return false;

                if (fi == null)
                {
                  FileInfo lastWrittenFile = null;
                  FileInfo[] fiArray = di.GetFiles("*.xml");

                  //find most recently written file
                  foreach (FileInfo fii in fiArray)
                  {
                    if (lastWrittenFile == null)
                      lastWrittenFile = fii;

                    if (fii.LastWriteTime > lastWrittenFile.LastWriteTime)
                      lastWrittenFile = fii;
                  }

                  this.ReadXml(lastWrittenFile.FullName);
                  return true;
                }
                else
                {
                  this.ReadXml(fi.FullName);
                  return true;
                }
            }
            catch (Exception ex)
            {
                return false;
            }
        }

        /// <summary>
        /// Populates dataset's InstalledSoftware table with data from registry
        /// </summary>
        /// <returns>false if there was an error</returns>
        public bool PopulateFromRegistry()
        {
            string uninstallKey = @"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall";
            string displayName, displayVersion;
            using (RegistryKey rk = Registry.LocalMachine.OpenSubKey(uninstallKey))
            {
                foreach (string skName in rk.GetSubKeyNames())
                {
                    using (RegistryKey sk = rk.OpenSubKey(skName))
                    {
                        List<string> names = new List<string>(sk.GetValueNames());

                        if (names.Contains("DisplayName"))
                            displayName = sk.GetValue("DisplayName").ToString();
                        else
                            continue;

                        if (names.Contains("DisplayVersion"))
                          displayVersion = sk.GetValue("DisplayVersion").ToString();
                        else                          
                          displayVersion = GetVersionFromName(displayName);
                            

                        //population of dataset
                        try
                        {
                            this.InstalledSoftware.AddInstalledSoftwareRow(displayName, displayVersion, false, false);
                        }
                        catch (Exception exc)
                        {
                            continue; //TODO error handling!
                        }
                    }
                }
            }

            return true;
        }

      /// <summary>
      /// Looks for a last word looking like a verion number (e.g. "1.12") 
      /// </summary>
      /// <param name="displayName">Program name including version value</param>
      /// <returns>empty string ("") if the word wasn't found</returns>
      private string GetVersionFromName(string displayName)
      {
        char[] separator = {' '};
        string[] words = displayName.Split(separator, 100);

        for (int c = words.GetLength(0) - 1; c >= 0; c--)
          if(words[c].Contains("."))
          {
            if (words[c].StartsWith("v", true, System.Globalization.CultureInfo.InvariantCulture))
              words[c] = words[c].Substring(1);
            return words[c];
          }
        
        return "";
      }      

      /// <summary>
      /// Returns index of the first record containing given application name
      /// </summary>
      /// <param name="appName">this string will be looked up in InstalledSoftware[c].sName member</param>
      /// <returns>-1 if nothing found</returns>
      public int IndexOf(string appName)
        {
        for(int c = 0; c < this.InstalledSoftware.Count; c++)
          if(this.InstalledSoftware[c].sName.Contains(appName))
            return c;

          return -1;
        }
    }
}

