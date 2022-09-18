package thread;

import java.io.File;

public class ThreadEx implements Runnable{
	
	public ThreadEx() {
		
	}
	

	@Override
	public void run() {
		String threadName=Thread.currentThread().getName();
		System.out.println("threadName >>> : "+threadName);
		
		try {
				for (int i=0; i<11; i++){
					Thread.sleep(1000);
					System.out.println(i+"초 경과하였음.");
				}
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				System.out.println("쓰레드 종료");
				e.printStackTrace();
			}
	}
}
