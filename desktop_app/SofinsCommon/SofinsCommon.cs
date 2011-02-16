using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;
using System.Xml;

namespace SofinsCommon
{
    public class SofinsCommon
    {

      public static bool PostXMLFileToSite(FileInfo fi)
      {
        if (fi == null || !fi.Exists)
          return false;

        try
        {
          SofinsDS sds = new SofinsDS();
          sds.LoadFromAppDataFolder(fi.Directory, fi);
          string dsAsString = sds.GetXml();


          System.Net.WebRequest reqPOST = System.Net.WebRequest.Create(@"http://2.homer.cz8.ru/api/programs");
          reqPOST.Method = "POST"; // Устанавливаем метод передачи данных в POST
          reqPOST.Timeout = 120000; // Устанавливаем таймаут соединения
          reqPOST.ContentType = "text/xml"; // указываем тип контента
          // передаем список пар параметров / значений для запрашиваемого скрипта методом POST
          // здесь используется кодировка cp1251 для кодирования кирилицы и спец. символов в значениях параметров
          // Если скрипт должен принимать данные в utf-8, то нужно выбрать Encodinf.UTF8
          byte[] sentData = Encoding.UTF8.GetBytes(dsAsString);
          reqPOST.ContentLength = sentData.Length;
          System.IO.Stream sendStream = reqPOST.GetRequestStream();
          sendStream.Write(sentData, 0, sentData.Length);
          sendStream.Close();

          System.Net.WebResponse result = reqPOST.GetResponse();

          return true;
        }
        catch (Exception ex)
        {
          return false;
        }

        //System.Net.WebClient wc = new System.Net.WebClient();
        //wc.Credentials = new System.Net.NetworkCredential("usr", "mypassword");
        //byte[] response = wc.DownloadData("http://localhost/testlogin");

        //CookieContainer cookies = new CookieContainer();
        //Request.CookieContainer = cookies;
        //// И после каждого запроса обновляем контейнер:
        //cookies = Request.CookieContainer;
      }
    }
}
