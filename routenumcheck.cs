using System;
using System.IO;
using System.Reflection;
using System.Text;

namespace RouteProcessor
{
    public static class RouteCompiler
    {
        public static string CompileRouteNumbers(string grab)
        {
            string assemblyFolder = Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location);
            
            string routeNumTxtPath = Path.Combine(assemblyFolder, "localdata", "routenum.txt");

            if (!File.Exists(routeNumTxtPath) || string.IsNullOrEmpty(grab) || grab.Length < 11)
                return string.Empty;

            string[] lines = File.ReadAllLines(routeNumTxtPath);
            StringBuilder lists = new StringBuilder();

            foreach (string line in lines)
            {
                if (line.Contains(grab.Substring(0, 11)))
                {
                    string grab1 = line.Trim();
                    if (grab1.Length >= 6)
                    {
                        string lastSix = grab1.Substring(grab1.Length - 6);
                        string cleaned = lastSix.Replace("/", "");
                        lists.Append($"{cleaned}, ");
                    }
                }
            }

            return lists.ToString();
        }
    }
}
