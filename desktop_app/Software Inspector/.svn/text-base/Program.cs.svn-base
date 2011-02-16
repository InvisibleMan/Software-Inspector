using System;
using System.Collections.Generic;
using System.Windows.Forms;
using System.IO;
using System.Threading;
using System.Data;
using SofinsCommon;

namespace Software_Inspector
{
    static class Program
    {
        /// <summary>
        /// state of the pc before current launch of the program
        /// </summary>
        public static SofinsDS previousState;

        /// <summary>
        /// state of the pc during current launch of the program
        /// </summary>
        public static SofinsDS currentState;
        public static string appDataFolder;

        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main(string[] args)
        {
            //init datasets for later use 
            previousState = new SofinsDS();
            currentState = new SofinsDS();
            
            appDataFolder = Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData);
            appDataFolder = Path.Combine(appDataFolder, "Sofins");

            Properties.Settings.Default.computerID  = Properties.Settings.Default.computerID ;


                if (currentState.PopulateFromRegistry() == false)
                    MessageBox.Show("Unable to get the list of installed programs from registry!");

                Application.EnableVisualStyles();
                Application.SetCompatibleTextRenderingDefault(false);
                Application.Run(new SoftwareInspectorForm());

        }
    }
}
