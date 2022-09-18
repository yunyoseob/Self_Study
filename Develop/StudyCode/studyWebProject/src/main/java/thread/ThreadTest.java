package thread;

import java.io.File;

public class ThreadTest {
	private static String fileStorepath="C:\\studyProject\\studyProject_work\\studyWebProject\\src\\main\\java\\file\\fileStore";
	
	public void fileMethod(){
		/*
		Runnable runable1=new ThreadEx();
		Thread thread1=new Thread(runable1);
		thread1.setName("Thread #1");
		
		thread1.start();
		*/
		
		String fileName="test7.bak";
		String filePath=fileStorepath+File.separator+fileName;
		String str="1,2,3,4,5, a,b,c,d,e,f,g \n h,i,j,k,l,m,n,o,p";
		
		try {
			File file=new File(filePath);
			
			if(!file.exists()){
				file.createNewFile();
				
				Runnable runable1=new ThreadFileTest(file, str);
				Thread thread1=new Thread(runable1);
				thread1.setName("Thread #2");
				
				thread1.start();
			}else {
				System.out.println("이미 파일이 존재합니다.");
				Thread.sleep(10000);
			}
		}catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public static void main(String[] args) {
		ThreadTest tTest=new ThreadTest();
		tTest.fileMethod();
	}
}
