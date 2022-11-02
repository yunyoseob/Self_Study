package jdme.common;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpSession;

public class K_Session {
	
	private static final String K_SESSION_ID = "KID";
	private static final String J_SESSION_ID = "JMNUM";
	
	
	//싱글톤 패턴
	private static class LazyHolder{//@@@@클래스 입니다! 클래스 속의 클래스@@@@
		public static final K_Session SESSIONLISTENER_INSTANCE = new K_Session();
	}
	
	public static K_Session getInstance() {
		return LazyHolder.SESSIONLISTENER_INSTANCE;
	/*
	의미 :  1. getInstance()의 리턴 값 : new K_Session()  (인스턴스, 메모리올리기)
	 	  2. 근데 이걸 상수로 박아놨음 
	 	  3. 상수는 변하면 안되는 값, 변하지 않는 값
	 	  ==> 어디서 인스턴스를 하던 항상 같은 '주소값'을 가지게 한다 
	*/
	}
	
	
	
	public K_Session() {
		//super()는 부모 클래스의 생성자를 호출하는 메서드입니다. 
		super();
	}
	
	public void killSession(final HttpServletRequest hReq) {
		/*
			getSession(boolean create) 
			:필요한 경우 이 요청에 대한 새 세션을 만들려면 boolean create(파라미터) true를 넣으면 됩니다.
			 false를 넣을 경우, 만약 session이 존재하지 않는다면 null을 반환합니다. 
			 ex) hreq(요청객체).getSesison(true) : 세션을 만듬
			 	 hreq(요청객체).getSession(false) : 세션이 존재하지 않을 경우 null반환
			cf) create=false를 넣었는데, session 존재할 때의 값은 test해보지 않았음.
		 */
		
		HttpSession hSession = hReq.getSession(false);//Session이 없다면, null이 뜰 것.
		
		//if(hSession!=null) : 위에서 보인 hReq.getSession(false)가 null이 아니다 = session값을 갖고 있다. = true로 구현체가 수행
		if(hSession !=null) {
			//removeAttribute(세션ID)
			//이 세션에서 지정된 이름으로 바인딩된 개체를 제거합니다. 
			//세션에 지정된 이름으로 바인딩된 개체가 없으면 이 메서드는 아무 작업도 수행하지 않습니다.
			hSession.removeAttribute(K_SESSION_ID);
			//invalidate();
			//이 세션을 무효화한 다음 바인딩된 모든 개체의 바인딩을 해제합니다.
			hSession.invalidate();
		}
	}
	
	public boolean setSession(final HttpServletRequest hReq, final String userID, final String unserNum) {
		/*
		 * getSession() : 해당 개체에 HttpSession을 요청, 
		 * 있으면 세션값을 반환, 이 요청과 관련된 현재 세션을 반환하거나 
		 * 요청에 세션이 없으면 세션을 '생성'합니다. 위에 getSession(boolean create)랑은 다른 녀석이다.(boolean create=true일 때는 같은 일을 함.)
		 * 세션 만들겠다는 뜻
		 */
		
		//아랫 줄 결과 : 1. 세션을 반환했거나(주소값) 2. 새롭게 생성되었을 것이다.
		HttpSession hSession = hReq.getSession();
		
		/* getAttribute() : 
		 * ::이 세션에서 지정된 이름으로 바인딩된 개체를 반환하거나 해당 이름으로 바인딩된 개체가 없으면 null을 반환합니다.
		 * 1. 세션이 이미 존재했다면 K_SESSION_ID에 대한 값을 가지는지 확인, 있다면 not null(어떤 값이 있겠지.)
		 * 1.1 K_SESSION_ID에 대한 값이 만약 없다면 null
		 * 2 새롭게 생성된 세션에도 한번 돌려봄, 당연히 null (세션부여 안했으니까.)
		 */
		String k_session_val = (String)hSession.getAttribute(K_SESSION_ID);
		int nCnt = 0;
		
		//K_SESSION_ID에 대한 value값이 있는가?
		if(k_session_val !=null) {
			//이 세션에 지정된 이름(KID의 value)과 userID가 같는가?
			boolean b1 = k_session_val.equals(userID);
			//만약 위 b1이 맞다면
			if(b1) {
				//0=>1
				nCnt++;
			}else {
				//k_session_val이 존재 하긴하는데(K_SESSION_ID=Const KID),로그인 한 userID랑 다름
				System.out.println("세션없음 >>> : ");
			}
		}else {//k_session_val이 처음부터 null일 경우=K_SESSION_ID에 대한 값이 아예 없을 경우
			System.out.println("세션 없음 >>> : ");
		}


		//nCnt==0 :: Session이 없을 경우
		if(nCnt==0) {
			/*setAttribute();
			지정된 이름을 사용하여 이 세션에 개체를 바인딩합니다. 
			같은 이름의 개체가 이미 세션에 바인딩되어 있으면 개체가 바뀝니다.
			*/
			hSession.setAttribute(K_SESSION_ID, userID);//K_SESSION_ID=KID=userID, Key&value
			hSession.setAttribute(J_SESSION_ID, unserNum);
		
			/*세션유통기한설정*/
			hSession.setMaxInactiveInterval(60*60); // 9시간 
			
			return false;
		}
		return true;
	}
	
	
	public String getSession(final HttpServletRequest hReq) {
		String strSession0 = "";
		String strSession1 = "";
		String strSession2 = "";
		//너 세션있니? : 없으면 null뜰거임
		HttpSession hSession = hReq.getSession(false);
		
		//만약 세션이 존재한다면(false인자를 줬음에도 null이 뜨지 않는다면 세션이 존재한다는 뜻이니까)
		if(hSession !=null) {
			//K_SESSION_ID에 대한 값을 줘(없을 수도 있음. 없으면 strSession=null)
			strSession1 = (String)hSession.getAttribute(K_SESSION_ID);
			strSession2 = (String)hSession.getAttribute(J_SESSION_ID);
			strSession0 = strSession1 + " : " + strSession2;
			}//strSession은, K_SESSION_ID에 대한 값을 가질 수도 있고, 없으면 null
		return strSession0;
	}
	
}
