package fileTest;

import java.io.File;
import java.io.FileWriter;

public class FileTest {
	private static String filePath="C:\\studyProject\\studyProject_work\\studyWebProject\\src\\main\\java\\file\\fileTest";
	
	public static void main(String[] args) {
		String outfile=filePath+File.separator+"test1.bak";
		
		FileWriter fw=null;
		
		try {
			File file=new File(outfile);
			file.createNewFile();
			
			String str="1,2,3,4,5, a,b,c,d,e";
			
			if(file.exists()){
				System.out.println("파일 생성 완료 >>> : "+file);
				fw=new FileWriter(file, true);
				fw.write(str);
				fw.close();
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
