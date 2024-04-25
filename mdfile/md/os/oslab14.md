---
title: oslab14

---

# oslab14

>  lab1
```java=
class Sync {
    public synchronized void add() {
        lab1.c++;
    }
    public synchronized void sub() {
        lab1.c--;
    }
}
class Job2 implements Runnable {
    private final Sync sync;
    private final int type;
    public Job2(Sync sync, int type) {
        this.sync = sync;
        this.type = type;
    }
    public void run() {
        if (sync != null) {
            if (type == 0) {
                run1();
            } else {
                run2();
            }
        }
    }
    private void run1() {
        for (int i = 0; i < 25000000; i++) {
            sync.sub();
        }
    }
    private void run2() {
        for (int i = 0; i < 25000000; i++) {
            sync.add();
        }
    }
}

public class lab1 {
    public static int c = 0;
    public static void main(String[] args) {
        Sync sync = new Sync();
  	  Job2 j = new Job2(sync, 0);
	Job2 j1 = new Job2(sync, 1);
        Thread t1 = new Thread(j);
        Thread t2 = new Thread(j);
        Thread t3 = new Thread(j1);
        Thread t4 = new Thread(j1);
        t1.start();
        t2.start();
        t3.start();
        t4.start();
        try {
            t1.join();
            t2.join();
            t3.join();
            t4.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println(c);
    }
}

```



>  lab2
```java=
import java.util.concurrent.locks.*;

class Warehouse //it's a monitor

{

	private Lock lock = new ReentrantLock();

	private Condition threadCond = lock.newCondition();

	private int product =0;

	public void setProduct()

	{

		lock.lock();

		try

		{

			while(product== 10) // warehouse is full, so wait

			{

				try

				{

					System.out.printf("FULL %n");

					threadCond.await();	

				}

				catch (InterruptedException e) {e.printStackTrace();}

			}





			product = product + 1; //set product

			System.out.printf("product +1 / amount = %d %n",product);

			threadCond.signal();

		}

		finally

		{

			lock.unlock();

		}

	}

	public void getProduct()

	{

		lock.lock();

		try

		{

			while(product ==0)//warehouse is empty, so wait

			{

				try

				{	

					System.out.printf("EMPTY %n");

					threadCond.await();

				}catch (InterruptedException e){e.printStackTrace();}

			}

			product=product-1; //get product

			System.out.printf("product -1 / amount = %d %n", product);

			threadCond.signal();

		}

		finally

		{

		lock.unlock();

		}

	}

}

class Job2 implements Runnable {

    private final Warehouse sync;
    private final int type;

		public Job2(Warehouse sync, int type) {
        this.sync = sync;
        this.type = type;
    }

    public void run() {
        if (sync != null) {
            if (type == 0) {
                run1();
            } else {
                run2();
            }
        }
    }

    private void run1() {
        for (int i = 0; i < 25000000; i++) {
            sync.setProduct();
        }
    }

    private void run2() {
        for (int i = 0; i < 25000000; i++) {
            sync.getProduct();
        }
    }
}
public class lab2 {
    public static int c = 0;
    public static void main(String[] args) {
        Warehouse sync = new Warehouse();
        Job2 j = new Job2(sync, 0);
        Job2 j1 = new Job2(sync, 1);
        Thread t1 = new Thread(j);
        Thread t4 = new Thread(j1);
        t1.start();
        t4.start();
        try {
            t1.join();
            t4.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println(c);
    }
}
```

