import java.util.Linkedlist

public class Storage{
	private final int MAX_SIZE = 100;
	private LinkedList<Object> list = new Linkedlist<Object>();
	
	public void produce(int num){
		
		synchronized(list){
			while(list.size() + num > MAX_SIZE){
				System.out.println("��ʱ��������");
				try{
					list.wait()
				}
				catch(){
					
				}
			}
		}
		
			//�����������㣬����num����Ʒ
			for(int i = 1; i <= num; ++i){
				list.add(new Object());
			}
		
			list.notifyAll();
	}
	
	public void consume(int num){
		synchronized(list){
			while(list.size() < num){
				System.out.println("�ֿ�洢������")
				try{
					list.wait()
				}
				catch(){
					
				}
			}
			for(int i = 1; i < num; ++i){
				list.remove()
			}
			list.notifyAll();
		}
	}
	
	public LinkedList<Object> getList(){
		return list;
	}
	
	public void setList(Linkedlist<Object> list){
		this.list = list;
	}
	
	public int getMaxSize(){
		return MAX_SIZE;
	}
	
	
	
	
	
	public class Producer extends Thread{
		private int num;
		private Storage storage;
		
		public Producer(Storage storage){
			this.storage = storage;
		}
		
		public void run(){
			produce(num);
		}
		
		public void produce(int num){
			sotrage.produce(num);
		}
		
		//������num,storage��get set������ʡ��
		
		
	}	
}

public class Consumer extends Thread  
{  
    // ÿ�����ѵĲ�Ʒ����  
    private int num;  
  
    // ���ڷ��õĲֿ�  
    private Storage storage;  
  
    // ���캯�������òֿ�  
    public Consumer(Storage storage)  
    {  
        this.storage = storage;  
    }  
  
    // �߳�run����  
    public void run()  
    {  
        consume(num);  
    }  
  
    // ���òֿ�Storage����������  
    public void consume(int num)  
    {  
        storage.consume(num);  
    }  
  
    // get/set����  
    public int getNum()  
    {  
        return num;  
    }  
  
    public void setNum(int num)  
    {  
        this.num = num;  
    }  
  
    public Storage getStorage()  
    {  
        return storage;  
    }  
  
    public void setStorage(Storage storage)  
    {  
        this.storage = storage;  
    }  
}  



















