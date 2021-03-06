import org.jfugue.*; 
import java.io.*;
import java.util.Scanner;



public class MyMusicApp {

	public static void main(String[] args) throws IOException {
		
		final int DATAPOINTS = 1000; // number data points per word
		int WORDS = 1;
		for (int i = 0; i < args.length; i++)
			System.out.println(args[i]);
		System.out.println(args.length);
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
	        	String[] result = line.split(" ");
	        	// System.out.println(result.length);
		        if(result.length < WORDS*2)
		        {
		        	System.out.printf("Bad line. ");
		        	System.out.println(result.length);
		        	line = br.readLine();
		        	continue;
		        }
		        // System.out.println(line);
	            sb.append(line);
	            Scanner in = new Scanner(line);
	            
	            if (line.split("\\s+").length != WORDS * 2){
	            	System.out.println(line);
	            	line = br.readLine();
	            	continue;
	            }

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
	    		sortedPos[i][j] = data[i*2+1][j] + 20;	//dirty, filthy hack
	    	}
	    }
	    //transform
	    for(int j=0; j<count; j++){
	    	int pos = 4;
	    	while(pos > 4-WORDS) {
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
	    
	    
	    Pattern output = new Pattern("T180");
	    for(int i=0; i<WORDS; i++) {
	    	Sonifier sf = new Sonifier(instruments[i], data[i*2], data[i*2+1], sortedPos[i], count, i);
	    	output.add(sf.getPattern());
	    }
	    
	    Player player = new Player();
	    player.saveMidi(output, new File("sonification.midi"));
	    System.out.println("Midi saved");
		player.play(output);
		
	    //PlayPatterns test = new PlayPatterns();
	    //System.out.println(test.getPattern(0, new DataPattern(0,1)));
	    
	    //Pattern p1 = new Pattern("I[TROMBONE] V0 C1qa120 G5ha100 A5qa90 C4qa90 C5ha120");
		//player.play(p1);
		
	    
	}

}
