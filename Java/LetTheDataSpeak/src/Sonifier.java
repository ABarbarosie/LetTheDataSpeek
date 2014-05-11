import org.jfugue.*; 

public class Sonifier {
	int DATAPOINTS;
	int[] alone;
	int[] together;
	int[] sortedPos;
	int channel;
	String instrument;
	
	public Sonifier(String instr, int[] al, int[] tg, int[] srtd, int cnt, int cn) {
		DATAPOINTS = cnt;
		sortedPos = srtd;
		together = tg;
		alone = al;
		instrument = instr;
		channel = cn;
	}
	
	public Pattern getPattern() {
		Pattern result = new Pattern();
		return result;
	}
	
}
