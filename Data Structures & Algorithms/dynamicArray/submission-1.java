class DynamicArray {
    int[] array;
    int capacity;
    int size;

    public DynamicArray(int capacity) {
        array = new int[capacity];
        this.capacity = capacity;
        size = 0;
    }

    public int get(int i) {
        return array[i];
    }

    public void set(int i, int n) {
        array[i] = n;
    }

    public void pushback(int n) {
        if(size == capacity){
            resize();
        }
        array[size] = n;
        size++;
    }

    public int popback() {
        if(size > 0){
            size--;
        }
        return array[size];
    }

    private void resize() {
        capacity = capacity*2;
        int[] arrayNew = new int[capacity];
        for(int i = 0; i < size; i++){
            arrayNew[i] = array[i];
        }
        array = arrayNew;
    }

    public int getSize() {
        return size;
    }

    public int getCapacity() {
        return capacity;
    }
}
