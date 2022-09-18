package thread;

import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;

public class ThreadFileTest implements Runnable{
	/*
	 * 쓰레드 시작 -> 파일 읽기 -> 파일 읽다가 중단될시 쓰레드 일시중지 + 
	 * 현재읽은 위치 기억하기 -> 파일 쓰기 -> 파일 다 썼으면 다시 여기로 돌아와서 이미 파일
	 * 이 존재한다고 뜨게 하기 -> 쓰레드 휴식
	 * */
	private static File file=null;
	private static String txt=null;
	
	FileWriter fw=null;
	FileReader fr=null;
	
	int data=0;
	
	public ThreadFileTest(File file, String txt){
		this.file=file;
		this.txt=txt;
	}

	@Override
	public void run() {
		String threadName=Thread.currentThread().getName();
		System.out.println("threadName >>> : "+threadName);
		
		try {
			if(this.file.exists()){
				System.out.println("파일 생성 완료 >>> : "+this.file);
				fw=new FileWriter(file, true);
				fw.write(this.txt);
				fw.close();
				
				fr=new FileReader(this.file);
				
				while((data=fr.read())!=-1){
					System.out.println("data >>> : "+(char)data);
					// fr.mark(data);
				}
				ThreadTest tt=new ThreadTest();
				tt.fileMethod();
			}
		}catch(Exception e){
			e.printStackTrace();
		}finally {
			if(fw!=null) {
				try {
					fw.close();
				}catch(Exception e2) {
					System.out.println("FileWriter close error >> : "+e2.getMessage());
				}
			}
		}
	}
}
