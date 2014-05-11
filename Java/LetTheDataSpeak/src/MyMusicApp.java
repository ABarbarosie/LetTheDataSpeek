import org.jfugue.*; 
import java.io.*;
import java.util.Scanner;



public class MyMusicApp {

	public static void main(String[] args) throws IOException {
		
		final int DATAPOINTS = 550; // number data points per word
		int WORDS = 1;
		if (args.length == 1)
		{
			System.out.println("No words provided");
			System.exit(1);
		}
		else if (args.length > 1)
		{
			WORDS = args.length;
		}
		
		
		
		System.out.println(WORDS);
		
		// retrieve the instruments from args.
		String[] instruments = new String[args.length];
		for (int i = 0; i < args.length; i++)
		{
			instruments[i] = args[i];
			System.out.println(args[i]);
		}
		
		
		/**
		 * Extract data from file
		 */
		int[][] data;
		data = new int[WORDS*2][DATAPOINTS];
		int count;
		
		BufferedReader br = new BufferedReader(new FileReader("data.txt"));
	    try 
	    {
	        StringBuilder sb = new StringBuilder();
	        String line = br.readLine();

	        count = 0;
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
		            	for (int index = 0; index < WORDS*2; index++)
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
	            
	            line = br.readLine();
	        }
//	        String everything = sb.toString();
//	        System.out.println(everything);
	        
	        // printing data array
	        /*
	        for (int i = 0; i < WORDS*2; i++)
	        {
	        	for (int j = 0; j < count; j++)
	        	{
	        		System.out.printf("%d ",data[i][j]);
	        	}
	        		System.out.println();
	        }
	        */
	    } 
	    finally 
	    {
	        br.close();
	    }
	
	    
	    /*
	     * Generate an array that keeps the relative position of a word
	     * in comparison to the other words for each data point 
	     */
	    
	    int[][] sortedPos = new int[WORDS][count];
	    
	    //get raw data
	    for(int i=0; i<WORDS; i++) {
	    	for(int j=0; j<count; j++) {
	    		sortedPos[i][j] = data[i*2+1][j] + 10;	//dirty, filthy hack
	    	}
	    }
	    //transform
	    for(int j=0; j<count; j++){
	    	int pos = WORDS-1;
	    	while(pos >= 0) {
	    		int m=-1, mp=-1;
	    		for(int i=0; i<WORDS; i++)
	    			if(sortedPos[i][j] > m) {
	    				m = sortedPos[i][j];
	    				mp = i;
	    			}
	    		sortedPos[mp][j] = pos;
	    		pos--;
	    	}
	    }
	    
	    Pattern output = new Pattern();
	    for(int i=0; i<WORDS; i++) {
	    	Sonifier sf = new Sonifier(instruments[i], data[i*2], data[i*2+1], sortedPos[i], count, i);
	    	output.add(sf.getPattern());
	    }

		Player player = new Player();
		player.play(output);
		//Pattern p1 = new Pattern("I[TROMBONE] V0 C1qa120 G5ha100 A5qa90 C4qa90 C5ha120");
		//player.play(p1);
		
	    
	}

}
