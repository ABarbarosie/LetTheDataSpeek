//import org.jfugue.*; 
import java.io.*;
import java.util.Scanner;



public class MyMusicApp {

	public static void main(String[] args) throws IOException {
		
		final int DATAPOINTS = 163; // number datapoints per word
		
		// retrieve the words from args.
		String[] words = new String[args.length];
		for (int i = 0; i < args.length; i++)
		{
			words[i] = args[i];
		}
		
		
		/**
		 * Extract data from file
		 */
		int[][] data;
		data = new int[args.length][DATAPOINTS];
		
		BufferedReader br = new BufferedReader(new FileReader("data.txt"));
	    try 
	    {
	        StringBuilder sb = new StringBuilder();
	        String line = br.readLine();

	        int count = 0;
	        while (line != null) 
	        {
	            sb.append(line);
	            Scanner in = new Scanner(line);
	            try{
		            int val;
		            if (args.length == 1)
		            {
		            	val = in.nextInt();
		            	data[0][count] = val;
		            }
		            else
		            {
		            	for (int index = 0; index < args.length; index++)
		            	{
		            		val = in.nextInt();
			            	data[index][count] = val;
		            	}
		            }
	            }
	            finally
	            {
	            	in.close();
	            }
	            count++;
	            
	            sb.append("\n");
	            line = br.readLine();
	        }
//	        String everything = sb.toString();
//	        System.out.println(everything);
	        
	        // printing data array
/*	        for (int i = 0; i < args.length; i++)
	        {
	        	for (int j = 0; j < count; j++)
	        	{
	        		System.out.printf("%d ",data[i][j]);
	        	}
	        		System.out.println();
	        }*/
	    } 
	    finally 
	    {
	        br.close();
	    }
	
//		Player player = new Player();
//		Pattern pattern1 = new Pattern("I[CHIFF] V0 A B C");
//		Pattern song = new Pattern();
//		song.add(pattern1);
//		player.play(song);
//		System.exit(0);
//		// If using Java 1.4 or lower
	    
	    
	}

}