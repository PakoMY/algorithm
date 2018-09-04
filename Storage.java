import java.util.Linkedlist

public class Storage{
	private final int MAX_SIZE = 100;
	private LinkedList<Object> list = new Linkedlist<Object>();
	
	public void produce(int num){
		
		synchronized(list){
			while(list.size() + num > MAX_SIZE){
				System.out.println("暂时不能生产");
				try{
					list.wait()
				}
				catch(){
					
				}
			}
		}
		
			//生产条件满足，生产num个产品
			for(int i = 1; i <= num; ++i){
				list.add(new Object());
			}
		
			list.notifyAll();
	}
	
	public void consume(int num){
		synchronized(list){
			while(list.size() < num){
				System.out.println("仓库存储量不足")
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
		
		//下面是num,storage的get set方法，省略
		
		
	}	
}

public class Consumer extends Thread  
{  
    // 每次消费的产品数量  
    private int num;  
  
    // 所在放置的仓库  
    private Storage storage;  
  
    // 构造函数，设置仓库  
    public Consumer(Storage storage)  
    {  
        this.storage = storage;  
    }  
  
    // 线程run函数  
    public void run()  
    {  
        consume(num);  
    }  
  
    // 调用仓库Storage的生产函数  
    public void consume(int num)  
    {  
        storage.consume(num);  
    }  
  
    // get/set方法  
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



















