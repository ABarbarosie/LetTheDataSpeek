
public class DataPattern {
	int first;
	int second;
	public DataPattern(int f, int s) {
		first = f;
		second = s;
	}
	
	@Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof DataPattern)) return false;
        DataPattern key = (DataPattern) o;
        return first == key.first && second == key.second;
    }

    @Override
    public int hashCode() {
        int result = first;
        result = 31 * result + second;
        return result;
    }
}
