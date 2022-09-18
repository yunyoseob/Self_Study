# Ext_JS_Study 2편

version : 6.2.1.167

**✔ [Sencha 공식 홈페이지](https://www.sencha.com/)**


**✔ [Sencha Documentation](https://docs.sencha.com/)**

## 위젯

<hr>


**✔ 셀렉션(Selection)**

```javascript
Ext.grid.selection.Selection

// 엑셀의 스프레드시트처럼 자유롭게 그리드의 영역을 설정할 수 있도록 스프레드시트 모델(SpreadsheetModel)을 지원한다.

Ext.grid.selection.SpreadsheetModel
selection:spreadsheet
```

**✔ 트리패널(TreePanel)**

트리패널(TreePanel)은 데이터를 트리형태의 모양으로 출력한다. 클릭하여 하위 아이템을 접거나 펼칠 수 있다.

```javascript
Ext.tree.Panel
xtype:treepanel


// leaf : true일 경우, 폴더내 아이템, fasle 일 경우 폴더가 된다.
leaf:true // 폴더 내 아이템
leaf:false // 폴더

// 트리패널의 아이템을 선택하면 해당 아이템의 노드와 부모 노드를 읽어온다.
// 아이템이 클릭될 때 이벤트를 얻기 위해서는 트리패널이 아닌 트리뷰에서 읽어와야 한다.

viewConfig:{
    listeners:{
        itemclick:function(view, dataObj, item, index, eventObj){
            selectedItemNode=dataObj;
            selectedFolderNode=dataObj.parentNode;
        }
    }
}

// 데이터를 추가하기 위해서는 appendChild를 사용한다.
seletedFolderNode.appendChild({
    text:'추가메뉴',
    leaf:true
})

// 데이터를 삭제하기 위해서는 removeChlid를 사용한다.
selectedFolderNode.removeChild(selectedItemNode);
```

**✔ xtype을 사용하기 위해서는 클래스에 alias:widget.앨리어스명을 정의할 수도 있고, 혹은 xtype:앨리어스명으로 정의할 수도 있다.**



## 서버연동

<hr>

**✔ 서버에서 작업하기**

웹 애플리케이션을 개발할 경우 웹 서버가 설치되어 있는 개발 서버가 있어야 하고, 개발이 완료된 파일은 서버에 업로드하여 테스트 해야 한다.

```
1. 프로젝트를 생성한다.
2. app.json등 설정에 필요한 사항을 미리 변경한다.
3. 개발 모드로 빌드한다
4. 개발환경에서 설정과 관련된 환경이 바뀌지 않을 경우 곡 빌드할 필요는 없다. 하지만 일반적으로 테마나 차트 등을 추가함으로써 환경이 변경되므로 미리 필요한 환경설정을 마치고 업로드 하는 것이 편리하다. 자동으로 반영하려면 sencha app watch를 실행시킨 상태에서 수정할 경우 빌드가 자동으로 수행된다. 하지만 개발 서버를 자주 컴파일 하지는 않을 것이다.
5. 개발서버에 프로젝트 폴더를 모두 복사하여 톰캣 서버의 경로에 복사한다.
6. 개발서버의 파일을 프로젝트에서 제공하는 텍스트 툴을 이용하여 개발한다. 또는 SVN을 이용하여 로컬에 다운받을 경우 선호하는 텍스트 에디터나 웹스톰과 같은 툴을 사용한다. (웹스톰, 이클립스 등)
7. 개발이 완료되면 배포를 위해 개발서버에 개발된 파일을 내려받는다.
8. 테스트 서버가 있을 경우 테스트 모드로 빌드한다. 빌드가 완료되면 완료된 build->testing->프로젝트명 폴더를 복사하여 테스트 서버에 복사한다.
9. 테스트 모드에서 정상적으로 동작하는지 확인한다.
10. 운영모드로 빌드한 뒤, build->production->프로젝트명 폴더를 복사하여 운영 서버에 복사한다.
11. 운영 모드에서 정상적으로 동작하는지 확인한다.
```


## 데이터

<hr>

데이터 패키지는 스토어, 모델, 프록시로 구성된다.

```javascript
/*
스토어 : 데이터 저장소로 일반적으로 모델, 프록시와 함게 사용된다. 

모델 : 스토어가 데이터를 가져오기 위해서는 데이터에 부합되는 레이아웃이 필요하며 이 레이아웃을 정의하는 것이 모델이다.

프록시 : 서버와 통신하기 위해 서버의 주소 및 파라미터 등을 정의하는 것이 프록시다. 개발자에 따라 프록시를 모델에 넣고 사용하거나 스토어에 넣고 사용할 수도 있다.
*/

// 경로에 파일을 추가하기
// index.html, index.js, data.html
// 서버에서 데이터만 내려받으면 되므로, html, phpm, jsp, xml, json 파일이든 상관없다.

// 모델을 정의한다. create가 아닌 define임에 유의한다.(config 속성에 fields가 정의되어 있다.)

Ext.define('model',{
    extend:'Ext.data.Model',
    config:{
        fields:['name','email','phone','age']
    }
})

// 스토어를 생성한다.
// reader 속성은 type과 rootProperty를 가지고 있으며 rootProperty는 스토어가 저장할 데이터의 최상위 객체로 지정한다.
// autoLoad를 true로 할 경우, 생성과 동시에 서버로부터 데이터를 읽어오며 config 밖에 선언되어 있다.

var store=Ext.create('Ext.data.Store',{
    config:{
        proxy:{
            model:'model',
            type:'ajax',
            url:'./data.html,
            reader:{
                type:'json',
                rootProperty:'data'
            }
        }
    },
    autoLoad:true
})
```

- Proxy를 분리해 별도로 정의하여 사용할 수 있다.

**✔ 모델**

모델은 데이터의 형태 곧 스키마를 정의한다. 모델에는 데이터를 정의하기 위해 필드를 정의하여 갖고 있다. 필드를 이용하여 주고받을 데이터를 정의한다. 

- 하지만, 경우에 따라 모델을 만들지 않고 스토어에서 필드를 직접 정의하여 사용할 수 있다.

```javascript
fields:['field1','field2','field3']
```
데이터의  Field Type

|타입|설명|
|--|--|
|auto|기본속성|
|string|기본문자열|
|int|Integer 데이터|
|number|실수형 데이터|
|booelan|true/false|
|date|날짜|

```javascript
fields:[{
    name:'field1',
    type:'int'
}]
```

모델간의 관계를 정의하고 활용할 수 잇다. 관계형 데이터베이스를 사용하기 위해서 테이블간 조인(join) 관계가 성립한다. (클라이언트에서도 관계를 정의하고 활용할 수 있다.)

```javascript
Ext.define('BasicServerApp.model.Base',{
    extend:'Ext.data.Model',
    fields:[{
        name:'id'
        type:'int'
    }],
    // 스키마 정의
    schema:{
        namespace:'BasicServerApp.model',
        proxy:{
            type:'ajax',
            url:'/resources/userdata.json',
            reader:{
                type:'json',
                rootProperty:'data.user'
            }
        }
    }
});
// 사용자를 관리할 모델 정의
Ext.define('BasicServerApp.model.User',{
    extned:'BasicServerApp.model.Base',
    fields:[{
        ...
    }]
});

// foreign key를 reference:'User'를 이용해 설정

Ext.define('BasicServerApp.model.Hobby',{
    extend:'BasicServerApp.model.Base',
    fields:{
        name:'userId',
        type:'int',
        reference:'User'
    }
});
```

**✔ 스토어**

스토어는 데이터의 저장소 역할을 하며, 프락시를 포함할 수도 있다. 프락시와 같이 사용하지 않을 경우 자체적으로 데이터를 가지고 있을 수 있다. 이 경우 서버와 연동할 필요없이 바로 데이터를 정의하고 사용할 수 있으며 스토어안에 data를 이용하여 정의한다.

```javascript
// name 속성 간단히 정렬
sorters:['name']

// name 속성 역순 정렬
sorters:[{
    property:'name',
    directoin:'DESC'
}],

// 메소드를 이용하여 실시간 처리
store.sort('name', 'DESC;);

// 필터링 기능 추가
filters:[{
    property:'name',
    value:'홍'
}],

// 메소드를 이용하여 실시간으로 처리
store.filter('name', '홍');

// like 검색이 아닌 정확한 검색을 원할 경우 exactMatch를 속성으로 추가

filters:[{
    property:'name',
    value:'홍길동',
    exactMatch:true,
    caseSensitive:true

}],
```

**✔ 프록시**

프록시는 서버와 통신하기 위해 생성된 객체다. 프록시는 통신을 하기 위한 속성을 다음과 같이 가지고 있다.

```javascript
type:'ajax'
url:'서버의 경로'
reader:{
    type:'json',
    rootProperty:'읽어오려는 객체의 최사우이 경로'
}
```

> **로컬데이터의 경우 type** 

 서버 또는 로컬 데이터와 통신하기 위한 설정으로 로컬데이터의 경우 다음과 같은 종류가 있다.

```
LocalStorageProxy, SessionStorageProxy, MemoryProxy
```

> **서버와 통신하기 위한 type:**

```
Ajax, JsonP, Rest, Direct
```

- url은 데이터의 경로로 데이터만 인식할 수 있으면 상관이 없다. (.jsp, .do, .asp, .html 등)

- 🤔 [Json vs JsonP](https://cheershennah.tistory.com/155)

```
1. json : Java Script Object Notaion

key-value 한쌍으로 이루어진 데이터 오브젝트를 전달하기 위해 사용하는 개방형 표준 포맷

2. json : JSON with Padding

클라이언트 단이 아닌, 다른 도메인에 있는 서버로부터 데이터를 요청하는 경우 사용되는 데이터 포맷이다.

JSON 데이터를 클라이언트가 지정한 콜백함수로 감싸(padding) 클라이언트에 전송한다.

자바스크립트는 서로다른 도메인에 대한 요청을 보안상 제한한다. 개발을 하다보면 어절 수 없이 다른 도메인으로부터 데이터를 가져오는 상황이 발생하는데 이러한 이슈 때문에 JSONP방식을 사용한다.

callback은 서버에서 지원해 주어야 한다.
```

**✔ 프록시의 API 기능**

프록시의 api는 마치 REST 서비스를 다루듯이 만들어졌다. 

REST 서비스는 데이터를 하나의 객체처럼 다룬다. 

데이터를 조회하거나 생성, 변경, 삭제 역시 객체의 메소드 형식으로 처리한다.

Ext JS는 서버에서 제공하는 서비스가 REST가 아니더라도 REST와 유사한 형태의 API를 지원한다. 프록시에서 지원하는 API 기능은 서버와 자동 연동하는데 목적이 있다. 프록시에 api 속성을 추가한다.

```javascript
api:{
    read:'./date.html',
    create:'./create.html',
    update:'./update.html',
    destory:'./delete.html'
},
```


## MVC Architecture

<hr>

![image](https://user-images.githubusercontent.com/109064073/184266079-c2d047c9-599b-4ba2-accf-bd75d63c503a.png)

1. Ext JS는 MVC 아키텍처를 지원한다.

2. MVC 아키텍처의 목적은 유연함에 가장 큰 목적이 있다. 필요에 따라 해당 기능을 마치 컴포넌트처럼 교체할 수 있다면, 프로그램의 개발 및 유지보수에 유리할 것이다.

3. MVC 아키텍처는 모델과 뷰, 컨트롤러 3가지 역할을 분리하여 파일을 나누어 개발하는데 목적을 갖는다.

4. 웹 어플리케이션의 시작이자 내부의 컨트롤러 모델, 스토어, 뷰 등을 관리한다.

5. 처음 시작시 프로젝트 폴더의 app.js가 자동으로 /app/view/main/Main.js를 호출하여 화면의 뷰포트에 나타나도록 처리했다. 따라서 별도의 시작 뷰를 설정하지 않아도 뷰 화면이 나타난다.

6. 애플리케이션은 전역을 사용할 컨트롤러와 모델, 스토어를 설정할 수 있다. 설정하고 난 뒤 웹 애플리케이션 어디서든지 호출이 가능하다.

```
View는 화면을 구성하는 위젯 등을 표현한다.
Model은 데이터를 표현하기 위한 레이아웃을 나타낸다.
Store는 데이터의 저장소로 사용되며 경우에 따라 Model 또는 Store 내에서 proxy를 사용할 수 있다.
Controller는 View, Model, Store를 제어하고, 이벤트, 메소드 등을 구현하고 처리한다.
```

**✔ View 기반으로 만든 소스를 MVC 아키텍처로 변경하는 절차**

```
1. 뷰 화면을 create로 바로 생성하지 말고 모두 define으로 정의한다.
2. 뷰의 화면에서 모델, 스토어, 이벤트 등을 모두 제거한다.
3. 모델은 model 폴더에 정의한다.
4. 스토어는 store 폴더에 정의한다.
5. 애플리케이션에 모델, 스토어, 컨트롤러를 정의한다.
6. 컨트롤러에서 이벤트는 control에 정의한다. 사용하려는 위젯은 ref에 정의한다.
7. 컨트롤러에서 메소드를 구현하고 필요한 로직을 구현한다.
```

- Main.js 파일은 프로젝트 폴더에 app -> view -> main 폴더에 위치한다. 기본적으로 생성된 코드는 MVC 아키텍처 구조가 아닌 MVVM구조의 파일이다.

- 따라서, vier 폴더에서는 Main.js 파일 이외에 뷰컨트롤러와 뷰 모델 파일이 같이 위치하고 있다.

- Application.js에서 컨트롤러를 등록해야 한다. 이렇게 등록한 컨트롤러는 전역으로 사용할 수 있다. 또한 컨트롤러는 별도의 requires 없이 모든 뷰에 접근 할 수 있다.

**✔ MVC 아키텍처: 뷰의 위젯에 접근하기 위해 래퍼런스 사용**

1. MVC 아키텍처에서는 뷰의 위젯을 접근하기 위해 레퍼런스를 사용한다. 또한 뷰에서 설정한 이벤트를 사용하기 위해 컨트롤을 사용한다.

2. 컨트롤러가 뷰의 컴포넌트에 접근하기 위해서는 refs를 지원한다.

3. refs에 접근하려는 컴포넌트의 이름을 지정하고 쿼리문을 이용하여 실제 위젯의 위치를 지정한다.

```javascript
refs:[
    name:'fieldname[name=myname]',
    email:'fieldname[name=email]'
]

// refs에서 정의한 이름은 conifig 속성처럼 사용할 수 있다.

this.getName()
this.getEmail()

// 컨트롤러가 이벤트를 정의하는 방법은 controls를 이용한다. control에서는 쿼리문을 이용하여 이벤트의 대상을 정한 뒤 이벤트명과 호출하려는 콜백함수를 사용한다.

control:{
    'panel widget[name=myname]':{
        click:'onEventMethod'
    }
}
// onEventMethod가 AppController의 함수로 정의되어 있으면 해당 이벤트 발생시 호출된다.
```

- **서버로부터 데이터를 가져올 때 데이터의 레이아웃을 정의하는 것이 모델이다. 모델은 create가 아닌 define으로 정의하여 사용한다.**

- 버튼 클릭시 호출한다면 autoLoad:false

**✔ MVC 데이터 & 페이지 그리드**

일반적으로 페이지쿼리를 이용하여 페이지 단위로 처리한다. Ext JS에서도 페이지 쿼리를 이용한 속성을 지원한다.

```
page: 현재의 페이지를 나타낸다.
start: 데이터의 시작 위치를 나타낸다.
limit: 반환하려는 데이터의 건수를 나타낸다.
```

컨트롤러에 그리드와 페이지 버튼을 연결하고 조회 버튼을 클릭할 경우 스토어를 처음 호출하므로 load 메소드를 사용한다.

```javascript
onSearch:function(button, e, eOpts){
    var me=this;
    var nickName=this.getNickName().getValue();
    Ext.getStore('UserStore').load({
        params:{
            searchNickName:nickName,
        },
        callback:this.onGetUserInfo,
        scope:me
    });
},
// 다음페이지로 이동할 경우 
Ext.getStore('UserStore').nextPage({
    ...
});
// 이전페이지로 이동할 경우
onPrev:function(button, e, eOpts){
    var me=this;
    var nickName=this.getNickName().getValue();
    Ext.getStore('UserStore').previousPage({
        ...
    });
}
```

**✔ 라우팅 & URI Hash**

뒤로 가기 버튼을 클릭했을 때 JS 안에 움직였던 페이지는 모두 무시되고 html 기준으로 이전 주소로 이동한다면, Ext JS가 아닌 이전에 열어보았던 웹 페이지가 나타나게 된다.

라우팅 기법은 이러한 문제를 해결할 수 있는 기법이다.

> **라우팅**

Ext JS에서 라우팅이란 페이지의 특정 위치를 호출하는 &lt;a&gt; 태그의 '#' 호출 기능을 이용하는 것을 말한다.

>**URI Hash**

URI Hash란 URI페이지 뒤에 #을 이용하여페이지의 위치를 지정하는 태그의 추가 정보를 말한다.


## MVVM Architecture

<hr>

![image](https://user-images.githubusercontent.com/109064073/184269964-28ccc9c0-3c4f-4353-81e6-388f523f3f70.png)

**[MVC Architecture vs MVVM Architecture](https://www.sencha.com/blog/ext-js-5-mvc-mvvm-and-more/)**

1. MVVM은 기본적으로 MVC를 대체하기 위해 만들어진 아키텍처이다.

2. MVC가 모델, 뷰, 컨트롤러 구분하여 프로그래밍을 한다고 해도 각 뷰를 통제하는 컨트롤러를 제어하기 어렵고, 뷰와 컨트롤러가 N:N 구조로 만들어지다 보면 전체적인 구조가 복잡하게 얽히게 된다.

3. MVVM은 이러한 MVC 문제점을 개선하기 위해 모델과 컨트롤러를 뷰에 종속적인 구조로 구성한 뷰 기준의 아키텍처이다.

4. 뷰가 종료된다면 뷰 컨트롤러와 뷰 모델이 같이 사라지게 된다.

5. 뷰모델은 뷰가 보여주는 화면을 대신한다.

6. 뷰모델은 통신을 위한 레이아웃이 아니다.

7. 뷰 컨트롤러는 뷰의 이벤트나 필요한 메소드를 구현하여 뷰와 상호 연동한다. 뷰 컨트롤러는 전역적인 글로벌 컨트롤러와는 달리 자신과 연결된 뷰에 한하며 이벤트나 참조 등의 구현이 단순하다. 

8. **Reference를 이용하거나 뷰 모델의 data를 이용한 바인드를 이용하는 방법이 있다.**

### 1. 레퍼런스(Reference)를 이용한 제어

래퍼런스는 객체를 바로 지정하여 필요할 경우 객체를 제어하여 사용할 수 있다. (속성에 reference를 추가한다.)

```
Ext.ComponentQuery.query 대신 this.getReference를 사용하며 뷰의 위젯을 찾는 다면, userId를 입력받아 닉네임, 패스워드 이메일 위젯을 배치하고 속성에 reference를 추가한다.
```

**뷰에서 각 위젯에 부여한 reference 속성을 불러오기 위해 뷰 컨트롤러는 this.lookupReference를 이용하여 접근한다.**

```javascript
...
onSearch:function(obj, selObj){
    var me=this;
    var userId=this.lookupReference('userId').getValue();
    Ext.Ajax.request({
        url:'../ServerPage/ShowUser.jsp',
        params:{
            userId:userId
        },
        success:function(res){
            ...
        }
        fail:function(res){
            ...
        }
    })
}
```

**✔ Form submit**

폼으로 위젯의 데이터를 서버에 전송하려 한다면 submit을 사용한다. submit으로 보내는 과정은 기본적으로 name을 사용한다,. 폼에 위치한 위젯에 name을 지정하고 뷰 컨트롤러는 폼만 읽어와 처리하도록 한다.

폼을 보내기 위해 현재의 뷰를 읽어오거나 뷰 안의 일부 영역에 위치한 폼컨테이너를 읽어와 보낼 수 있다.

```
this.getView().getForm()
```

주의할 점은 폼이 최상위 뷰로 선언했다면 reference를 부여할 수 없다.

### 2. 바인드(Bind)를 이용한 구현

![image](https://user-images.githubusercontent.com/109064073/184270120-c9ea4f08-ccbc-4717-9fa5-26010385d107.png)

레퍼런스를 이용할 경우 객체를 참조하는 방식이었으나 바인드를 이용한 연동 방식은 값을 공유하는 방식이다.

- 값을 공유한다는 것은 위젯과 뷰 모델이 지정된 값을 공유하는 방식을 따른다.

```javascript
{
  xtype:'textfield',
  fieldLabel:'사용자 ID',
  labelAlign:'right',
  bind:'{userId}'
}

// 뷰 컨트롤러에 뷰 모델을 이용하여 값을 읽고 설정한다.

// 값을 읽어오는 방법
var userId=this.getViewModel().get('userId');

// 값을 설정하는 방법
me.getViewModel().set('nickName', obj.data.nickName);
```

### Store를 이용한 데이터 처리

![image](https://user-images.githubusercontent.com/109064073/184270942-1158a410-473d-49e4-b7ba-b61786b554e5.png)

1. Store를 추가하고 바인드로 연결한다. 

2. 스토어를 사용하기 위해서 뷰모델에 추가한다.

3. 이전에 글로벌 스토어가 아닌 뷰 모델 안에 스토어를 추가함으로써 스토어 역시 뷰가 종료될 경우 같이 메모리에서 종료된다.

4. 뷰모델에 추가한 스토어는 뷰에서 bind를 이용하여 연결할 수 있다.

5. 뷰 모델의 스토어는 주로 서버와 통신하기 위한 저장소 역할을 한다.

6. 데이터가 뷰와 연동되는 역할이라면 Store는 뷰와 아무런 관련이 없다.

> **뷰 모델 정의하기**

```javascript
viewModel:{
    type:'usershowlist'
},
// 스토어에 바인드를 하기
bind:{
    store:'{userInfo}'
}
```

뷰모델에 stores 안에 스토어를 정의한다. 서버와 연동하기 위한 처리가 한 개가 아닌 여러 개가 될 수 있으므로 stores 안에 필요한 만큼 정의하여 사용한다.

> **뷰 컨트롤러에서는 뷰모델의 스토어를 가져와 사용할 수 있다.**

```javascript
this.getViewModel().getStore('스토어명');
```

**✔ 바인드 & 포뮬러**

items라는 내부 컴포넌트에 이름을 주고 간단히 바인드 할 수 있었다.

실제로 bind 속성이 자동으로 바인드 해주기 때문에 쉽고 빠르게 사용할 수 있지만 내부 컴포넌트가 아니거나 속성이 단순하지 않을 경우 바인드를 해주는 것이 항상 편한 것은 아니다.

**뷰의 속성을 바인드 하기 : 뷰모델의 data에 공유속성 정의하기**

```javascript
data:{
    titleName:'',
    width:'',
    height:''
}

// 뷰의 속성을 공유하기 위해 bind를 이용해 감싸고 내부 속성을 {}을 이용하여 설정한다.

bind{
    title:'타이틀은 {titleName} 입니다.',
    width:'{width}',
    height:'{height}'
}

// 내부 컴포넌트에도 동일하게 적용할 수 있다.

data:{
    textName:'',
    width:'',
    height:''
}

// 뷰의 내부 아이템 속성을 공유하기 위해 bind를 이요해 감싸고 내부 속성을 {}을 이용하여 설정한다.

items:[{
    xtype:'button',
    bind:{
        text:'{textName}',
        width:'{width}',
        height:'{height}'
    }
}]

// 두 개의 값을 동시에 출력해보기

data:{
    tel1:'',
    tel2:'',
    tel3:''
},

formulas:{
    tel:function(get){
        return tel1 + '-' +tel2 + '-' +tel3;
    }
}

// 경우에 따라 formulas에 정의할 함수를 계산을 위한 용도로 사용할 수 있다.

items:[{
    xtype:'textfield',
    bind:'{tel}'
},{
    xtype:'hidden',
    bind:'{tel1}'
},{
    xtype:'hidden',
    bind:'{tel2}'
},{
    xtype:'hidden',
    bind:'{tel3}'
}]

// 동일한 방식으로 읽고 쓰기를 포뮬러스를 이용해 구현하기

data:{
    zpno1:'',
    zpno2:''
},
formulas:{
    zpno:{
        get:function(get){
            return tel1+'-'+tel2+'-'+tel3;
        },
        set:function(value){
            if(value.length!=6){
                return;
            }
        }
        this.set({
            zpno1:value.substring(0,3),
            zpno2:value.substring(3,6)
        });
    }
}
```

**✔ 참고**

1. 레퍼런스와 바인드 중 어떤 방식을 사용해도 된다.

2. 다만 바인드를 사용할 경우 경우에 따라 복잡성이 증가할 수 있다.


## MVVM과 MVC 연동

<hr>

1. MVVM은 뷰 단위로 구성되어 있기 때문에 전체적인 컨트롤 역할이 없는 상황이다.

2. 전체적인 애플리케이션을 구성하려면 중앙에서 컨트롤해야 할 필요성이 생긴다.(전체적인 중앙 컨트롤러가 없어도 뷰간 연동으로 구현할 수 있다.)

3. 이에 대한처리로 MVC 아키텍처를 MVVM 아키텍처에 접목하는 방법이 있을 수 있다.

4. 업무적인 화면은 MVVM에서 처리하고 공통적인 내용이나 뷰간 연동 등은 MVC에서 처리하는 방법이다.

**✔ MVC 아키텍처**

![image](https://user-images.githubusercontent.com/109064073/184284786-b5c90bf9-caa3-4e82-b129-1dc51559bbe0.png)

1. MVC 아키텍처의 경우 글로벌 컨트롤러는 모든 뷰에 접근할 수 있다. 따라서 웹앱 안의 모든 뷰를 접근하여 읽어오거나 설정할 수 있는 권한을 갖게 된다. 따라서 뷰가 많아지고 뷰의 그룹별로 컨트롤러가 관리될 때, 1:N 구성을 넘어서 N:N 구성으로 변경될 가능성이 높다. 이러한 구성은 복잡도를 증가시킨다.

**✔ MVVM 아키텍처 Reference를 이용한 구성**

![image](https://user-images.githubusercontent.com/109064073/184286002-2008344c-30ee-49b8-8016-9ed1566138b9.png)


1. 래퍼런스를 이용할 경우 뷰의 객체를 뷰 컨트롤러가 직접 접근하여 처리할 수 있다. 이 때 레퍼런스란 객체 자체를 가리키므로 객체를 찾은 뒤에는 객체가 제공하는 메소드를 이용하여 값을 읽거나 쓸 수 있다.

**✔ MVVM 아키텍처 Bind를 이용한 구성**

![image](https://user-images.githubusercontent.com/109064073/184286082-e8978a25-81d3-4f35-9f32-95f26665b38e.png)

1. 바인드의 경우 뷰 모델의 data가 뷰와 뷰 컨트롤러 간 값을 전달하는 역할로 객체가 아닌 값 기준의 연동이다.

2. 만약 MVVM의 바인드 변수가 값이 아닐 경우 이러한 처리방식은 복잡할 수 있으며 포뮬러를 이용해야 한다. 또한 MVVM은 스토어를 뷰에서 처리할 수 있도록 제공하고 있는데, 이 스토어 역시 뷰 모델에 종속되므로, 뷰가 종료되면 메모리에서 사라지게 된다.

**✔ MVVM+MVC 아키텍처**

![image](https://user-images.githubusercontent.com/109064073/184283591-5ac2078c-5331-4cf6-bbf1-364a4b2c41b7.png)

1. MVVM 아키텍처는 뷰 중심의 구성이다.

2. MVVM의 구성이 화면 단위의 업무용 프로그램을 만든다면 상단에 존재하는 MVC 아키텍처의 글로벌 컨트롤러는 공통 기능을 담당하게 된다.

3. 각 MVVM 프로그램에서 호출하여 사용할 수 있도록 메소드를 제공하며 뷰간 연동을 지원함으로써 구성을 단순화 시킬 수 있다.

> **메뉴 연동**

1. 뷰 간의 연결을 위해 기본적인 쿼리문을 이용해 사용하여 처리할 수 있다. 하지만 쿼리문을 매번 사용기 보다는 이러한 기능을 공통 기능으로 묶어 상대 파일명만 호출한다면 사용하기 훨씬 편리하다.

2. 공통기능은 전역적으로 관리하기 위해 글로벌 컨트롤러에 기능을 추가한다면 개발 및 관리가 훨씬 용이해진다.