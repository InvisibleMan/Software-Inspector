namespace Software_Inspector
{
    partial class SoftwareInspectorForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.ListFromRegistryListView = new System.Windows.Forms.ListView();
            this.ApplicationName = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.ApplicationVersion = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.listOfInstalledSoftwareLabel = new System.Windows.Forms.Label();
            this.RefreshFromRegistryButton = new System.Windows.Forms.Button();
            this.SaveAsAnXMLFile = new System.Windows.Forms.Button();
            this.saveFileDialogXML = new System.Windows.Forms.SaveFileDialog();
            this.ChangeSettingsButton = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // ListFromRegistryListView
            // 
            this.ListFromRegistryListView.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
                        | System.Windows.Forms.AnchorStyles.Right)));
            this.ListFromRegistryListView.Columns.AddRange(new System.Windows.Forms.ColumnHeader[] {
            this.ApplicationName,
            this.ApplicationVersion});
            this.ListFromRegistryListView.Location = new System.Drawing.Point(12, 40);
            this.ListFromRegistryListView.Name = "ListFromRegistryListView";
            this.ListFromRegistryListView.Size = new System.Drawing.Size(758, 204);
            this.ListFromRegistryListView.TabIndex = 0;
            this.ListFromRegistryListView.UseCompatibleStateImageBehavior = false;
            this.ListFromRegistryListView.View = System.Windows.Forms.View.Details;
            // 
            // ApplicationName
            // 
            this.ApplicationName.Text = "Name";
            this.ApplicationName.Width = 585;
            // 
            // ApplicationVersion
            // 
            this.ApplicationVersion.Text = "Version";
            this.ApplicationVersion.Width = 93;
            // 
            // listOfInstalledSoftwareLabel
            // 
            this.listOfInstalledSoftwareLabel.AutoSize = true;
            this.listOfInstalledSoftwareLabel.Location = new System.Drawing.Point(12, 13);
            this.listOfInstalledSoftwareLabel.Name = "listOfInstalledSoftwareLabel";
            this.listOfInstalledSoftwareLabel.Size = new System.Drawing.Size(326, 17);
            this.listOfInstalledSoftwareLabel.TabIndex = 1;
            this.listOfInstalledSoftwareLabel.Text = "List of installed software (according to the registry)";
            // 
            // RefreshFromRegistryButton
            // 
            this.RefreshFromRegistryButton.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.RefreshFromRegistryButton.Location = new System.Drawing.Point(12, 260);
            this.RefreshFromRegistryButton.Name = "RefreshFromRegistryButton";
            this.RefreshFromRegistryButton.Size = new System.Drawing.Size(262, 41);
            this.RefreshFromRegistryButton.TabIndex = 2;
            this.RefreshFromRegistryButton.Text = "Refresh list from Registry";
            this.RefreshFromRegistryButton.UseVisualStyleBackColor = true;
            this.RefreshFromRegistryButton.Click += new System.EventHandler(this.RefreshFromRegistryButton_Click);
            // 
            // SaveAsAnXMLFile
            // 
            this.SaveAsAnXMLFile.Location = new System.Drawing.Point(15, 332);
            this.SaveAsAnXMLFile.Name = "SaveAsAnXMLFile";
            this.SaveAsAnXMLFile.Size = new System.Drawing.Size(199, 38);
            this.SaveAsAnXMLFile.TabIndex = 3;
            this.SaveAsAnXMLFile.Text = "Save list as an XML file";
            this.SaveAsAnXMLFile.UseVisualStyleBackColor = true;
            this.SaveAsAnXMLFile.Click += new System.EventHandler(this.SaveAsAnXMLFile_Click);
            // 
            // saveFileDialogXML
            // 
            this.saveFileDialogXML.DefaultExt = "xml";
            this.saveFileDialogXML.Filter = "XML files|*.xml";
            this.saveFileDialogXML.FileOk += new System.ComponentModel.CancelEventHandler(this.saveFileDialogXML_FileOk);
            // 
            // ChangeSettingsButton
            // 
            this.ChangeSettingsButton.Location = new System.Drawing.Point(303, 260);
            this.ChangeSettingsButton.Name = "ChangeSettingsButton";
            this.ChangeSettingsButton.Size = new System.Drawing.Size(224, 41);
            this.ChangeSettingsButton.TabIndex = 4;
            this.ChangeSettingsButton.Text = "Change settings";
            this.ChangeSettingsButton.UseVisualStyleBackColor = true;
            this.ChangeSettingsButton.Click += new System.EventHandler(this.ChangeSettingsButton_Click);
            // 
            // SoftwareInspectorForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(782, 435);
            this.Controls.Add(this.ChangeSettingsButton);
            this.Controls.Add(this.SaveAsAnXMLFile);
            this.Controls.Add(this.RefreshFromRegistryButton);
            this.Controls.Add(this.listOfInstalledSoftwareLabel);
            this.Controls.Add(this.ListFromRegistryListView);
            this.MaximumSize = new System.Drawing.Size(800, 480);
            this.MinimumSize = new System.Drawing.Size(800, 480);
            this.Name = "SoftwareInspectorForm";
            this.Text = "Software Inspector";
            this.FormClosed += new System.Windows.Forms.FormClosedEventHandler(this.SoftwareInspectorForm_FormClosed);
            this.Load += new System.EventHandler(this.RefreshFromRegistryButton_Click);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.ListView ListFromRegistryListView;
        private System.Windows.Forms.Label listOfInstalledSoftwareLabel;
        private System.Windows.Forms.Button RefreshFromRegistryButton;
        private System.Windows.Forms.ColumnHeader ApplicationName;
        private System.Windows.Forms.ColumnHeader ApplicationVersion;
        private System.Windows.Forms.Button SaveAsAnXMLFile;
        private System.Windows.Forms.SaveFileDialog saveFileDialogXML;
        private System.Windows.Forms.Button ChangeSettingsButton;
    }
}

