import java.io.File;
import java.io.FileWriter;
import java.util.Scanner;

public class qgraph {
    public static void main(String[] args) throws Exception {
        //===================================================
        //=       Step 0: Get CSV root & Initalize          =
        //===================================================
        Scanner uin = new Scanner(System.in);
        String[] call =  {"python3", "../python/qplot.py"};
        //String[] cleancall = {"cd ..", "cd ./python", "rm passoff.txt && rm csvpaths.txt", "cd ..", "cd ./bin", "rm pylog.txt"};
        String gname = null;
        String gnumstring = null;
        System.out.print("Please point to the directory contaning the CSV's of interest : ");
        String csvdir = uin.nextLine();
        System.out.print("Is ==> "+csvdir+" : the correct directory? yes (y)/ no (n)/ quit (q) : ");
        String cnfirm0 = uin.nextLine();
        if (cnfirm0.contains("n")) {
            while (cnfirm0.contains("n")) {
                System.out.print("Please enter the corrected directory : ");
                csvdir = uin.nextLine();
                System.out.print("Is ==> "+csvdir+" : the correct directory? yes (y)/ no (n)/ quit (q) : ");
                cnfirm0 = uin.nextLine();
                if (cnfirm0.contains("q")) {
                    System.out.println("Exiting... Goodbye");
                    System.exit(0);
                 }
            }
        } else if (cnfirm0.contains("q")) {
            System.out.println("Exiting... Goodbye");
            System.exit(0);
        } 
        //===================================================
        //=       Step 1: Build CSV Paths                   =
        //===================================================
        File rpath = new File(csvdir);
        String[] csvext = rpath.list();
        String[] csvpaths = new String[csvext.length];

        //===================================================
        //=       Step 2: Get Data & Write txt for python   =
        //===================================================
        FileWriter passcsvs = new FileWriter("../python/csvpaths.txt");
        for (int x = 0 ; x < csvext.length ; x++) {
            csvpaths[x] = csvdir +"/"+ csvext[x];
            passcsvs.write(csvpaths[x] + "\n");
        }
        passcsvs.close();
        FileWriter passoff = new FileWriter("../python/passoff.txt");
        if (csvext.length > 1) {
            System.out.print("How many unique graphs : ");
            gnumstring = uin.nextLine();
            System.out.print("Graph Name : ");
            gname = uin.nextLine();
            passoff.write("Number of CSV's : " + Integer.toString(csvext.length) + "\n" + "Name of Graph : " + gname  + "\n"  +  "Number of Graphs : " + gnumstring);
        } else if (csvext.length == 1) {
            System.out.print("Graph Name : ");
            gname = uin.nextLine();
            passoff.write("Number of CSV's : " + "\n" + "Name of Graph : " + gname + "Number of Graphs : 1");
        }
            passoff.close();
        //c
        //===================================================
        //=       Step 3: Begin Executing Python Script     =
        //===================================================
        Process pyexc = Runtime.getRuntime().exec(call);
        File fpath = new File("../plots/"+ gname +".svg");
        int cnt = 0;
        while (fpath.canRead() != true) {
            if (cnt == 0) {
            System.out.println("Waiting for python to finish it's business...");
            }
            cnt += 1;
            if (cnt == 20000) {
                System.exit(0);
            }
        }
        System.out.println("Plots found! finishing up...");
        //CLEANUP
        
        //TEMP end
        uin.close();
        System.out.println("Allgedly we have cleaned up");
    }
}
