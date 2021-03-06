//import java.util.ArrayList;
//import java.util.HashMap;

import org.jfugue.*; 

public class Sonifier {
	int DATAPOINTS;
	int[] alone;
	int[] together;
	int[] sortedPos;
	int channel;
	String instrument;
	PlayPatterns playPat;
	
	public Sonifier(String instr, int[] al, int[] tg, int[] srtd, int cnt, int cn) {
		DATAPOINTS = cnt;
		sortedPos = srtd;
		together = tg;
		alone = al;
		instrument = instr;
		channel = cn;
		playPat = new PlayPatterns();
	}
	
	//get the corresponding pattern to 3 notes
	public DataPattern getDataPattern(int a, int b, int c) {
		return new DataPattern(Integer.signum(b-a), Integer.signum(c-a));
	}
	
	//get the not corresponding to a certain noteNumber
	public String getNote(int noteNum) {
		
		if(noteNum<0) return "C1";
		
		char name; int octave;
		int n = noteNum % 7;
		if(n<5) name = (char)((int)'C' + n);
		else name = (char)((int)'A' + n - 5);
		
		octave = noteNum/7 + 2;
		
		String result = name + Integer.toString(octave);
		return result;
	}
	
	//get the noteNumber corresponding to a certain datapoint
	public int getNoteNum(int datapoint) {
		return (int)((double)35/100 * (double)datapoint);
	}
	
	//convert a musical pattern with a root note and volume to actual notes
	public String rawToNotes(NotePair[] playPattern, int root, int attack) {
		String res = "";
		
		for(int i=0; i<playPattern.length; i++) {
			int curn = root + playPattern[i].val;
			res += ' ' + getNote(curn) + playPattern[i].dur + 'a' + Integer.toString(attack);
		}
		return res;
	}
	
	//get the entire pattern for an instrument
	public Pattern getPattern() {
		String res = "";
		res += "I[" + instrument + "] ";
		res += "V" + Integer.toString(channel);
		
		//for each triplet of datapoints
		for(int i=0; i+2<DATAPOINTS; i+=3){
			//get their contour
			DataPattern p = getDataPattern(alone[i], alone[i+1], alone[i+2]);
			//get the musical pattern
			NotePair[] playPattern = playPat.getPattern(sortedPos[i], p);
			//generate root note and volume by means
			int root = getNoteNum((alone[i] + alone[i+1] + alone[i+2])/3);
			int attack = (int)((double)0.84*(together[i]+together[i+1]+together[i+2])/3 + 42);
			
			//convert to notes and add 
			res += rawToNotes(playPattern, root, attack);
		}
		
		return new Pattern(res);
	}
	
}
