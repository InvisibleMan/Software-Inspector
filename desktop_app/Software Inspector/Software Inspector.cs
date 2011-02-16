using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using Microsoft.Win32;
using System.IO;

using SofinsCommon;

namespace Software_Inspector
{
    public partial class SoftwareInspectorForm : Form
    {
        public SoftwareInspectorForm()
        {
            InitializeComponent();
        }

        private void RefreshFromRegistryButton_Click(object sender, EventArgs e)
        {
            if (ListFromRegistryListView == null)
                ListFromRegistryListView = new ListView();

            if (Program.currentState == null)
            {
                Program.currentState = new SofinsDS();
                if (Program.currentState.PopulateFromRegistry())
                    return; //TODO error handling
            }

            foreach(SofinsDS.InstalledSoftwareRow isr in Program.currentState.InstalledSoftware)
            {
                //population of listview
                ListViewItem lv = this.ListFromRegistryListView.Items.Add(isr.sName);
                lv.SubItems.Add(isr.sVersion);
            }
        }

        private void SaveAsAnXMLFile_Click(object sender, EventArgs e)
        {
            DialogResult dr = saveFileDialogXML.ShowDialog();
        }

        private void saveFileDialogXML_FileOk(object sender, CancelEventArgs e)
        {
            Program.currentState.WriteXml(saveFileDialogXML.FileName);                        
        }

        private void SoftwareInspectorForm_FormClosed(object sender, FormClosedEventArgs e)
        {
            Program.currentState.SaveToAppDataFolder(new DirectoryInfo(Program.appDataFolder));
        }

        private void ChangeSettingsButton_Click(object sender, EventArgs e)
        {
            DotBits.Configuration.ConfigEditor c = new DotBits.Configuration.ConfigEditor(Properties.Settings.Default);
            c.ShowDialog(this);

        }
    }
}
