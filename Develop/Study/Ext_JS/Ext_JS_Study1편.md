# Ext_JS_Study 1편

version : 6.2.1.167

**✔ [Sencha 공식 홈페이지](https://www.sencha.com/)**


**✔ [Sencha Documentation](https://docs.sencha.com/)**


## Ext JS

<hr>

1. Ext JS는 고성능의 변형가능한 UI 위젯을 지원한다. 수 백개의 위젯이 지원되므로 고객이 요구하는 위젯의 기능을 그대로 사용하거나 변형하여 사용할 수 있다.

2. 다양한 백엔드 소스에 맞출 수 있는 데이터 패키지를 포함한다. 최소한의 조작으로 서버의 데이터를 가져와 사용할 수 있도록 지원한다.

3. 다양한 화면에 적합한 레이아웃 매니저와 설정을 지원한다. 반응형 레이아웃을 이용하여 데스크탑, 모바일 또는 화면 크기에 따른 세부적인 제어가 가능하다.

4. 진보된 차트 패키지를 지원한다. Ext JS 6는 수십개의 차트를 지원한다. 통합된 차트 기능은 설정파일의 requires를 호출함으로써 간단히 사용할 수 있다.

5. 쉽게 사용하거나 변경할 수 있는 테마를 지원한다. 테마에 대한 컴파일 SCSS를 이용하여 프로그램 가능한 CSS파일 생성이 가능하며 사용자 테마를 만들어 사용할 수 있다.

**✔ Ext JS, Sencha Touch 프레임워크 통합**

![image](https://user-images.githubusercontent.com/109064073/184115385-a47e6700-8ee8-4efb-aa00-a95e19ec76c5.png)


Classic : 데스크탑을 지원하는 것을 클래식 툴킷이라고 한다.

Modern : 모바일을 지원하는 것을 모던 툴킷이라고 한다.

View 영역은 Classic과 Modern이라는 두 개의 툴킷을 각각 제공한다. (다시말해 내부의 코어 프로그램은 데스크탑(classic)과 모바일(modern) 툴킷이 같이 사용할 수 있으며 화면의 맨 앞의 뷰는 서로 다른 코드를 이용하여 구현한다는 것을 의미한다.)

**✔ 센차 컴멘드**

센차 컴멘드를 이용하여 프로젝트를 만들고 컴파일한다. 컴파일을 해야만 css를 포함한 라이브러리의 용량을 최소화 할 수 있다.

**센차 컴멘드가 가지는 역할**

1. 작업공간 및 패키지를 관리한다.
2. 기본적인 애플리케이션의 기본형태를 만들고 코드를 생성하고 장애를 발견한다. 빌드 시 잘못된 코드를 확인 시켜준다.
3. 자바스크립트의 컴파일러, 애플리케이션 튜닝 그리고 이미지 반환 등을 지원한다.
4. 네이티브 팩킹을 지원하다. 네이티브 팩킹은 모바일 환경의 프로젝트 일 경우이며, 코르도바와 연동하여 배포 할 수 있다.

**✔ Ext JS의 3가지 컴파일 옵션**

```
sencha app build development (개발 모드)
sencha app build testing (테스트 모드)
sencha app build production (운영 모드)
```

## Ext JS : Class

<hr>

1. 클래스는 Ext.define 문을 이용하여 정의할 수 있다.

```javascript
Ext.define('클래스명', {...})
```

java로 비유하면 다음과 같다.

```java
class A{
    ...
}
```

2. 정의된 클래스를 생성하기 위해서는 Ext.create문을 사용한다.

```javascript
Ext.create('정의된 클래스', {...});
```

java로 비유하면 다음과 같다.

```java
A a = new A();
```
- **xtype:'앨리어스명'과 같이 앨리어스 명을 사용할 경우, Ext.create와 동일하다.**

3. 클래스는 일반속성과 config 속성을 가질 수 있다. **config 속성은 설정과 같은 속성으로 클래스 생성시 속성으로 인식 된다.**

```javascript
config:{
    name:null
}
```

4. config에 속성을 설정할 경우, 해당 속성은 자동으로 get, set 접두어를 붙여 메소드로 사용할 수 있다.

```javascript
this.getName(), this.setName('설정값')
```

5. 클래스가 정의될 때 생성자를 정의할 수 있다. 생성자 함수는 처음 클래스가 생성될 때 자동으로 반영하기 위해 constructor 생성자를 추가한다. constructor 생성자 안에 config 속성을 반영하기 위해 this.initConfig(config)를 호출 한다.

```javascript
constructor:function(config){
    this.initConfig(config)
}
```

### Ext JS : 상속

Ext JS는 수많은 클래스를 정의하고 상속을 통해 체계적으로 관리한다.

```javascript
Ext.define('새로운클래스'){
    extend:'상속받을 클래스',
});
```

### Ext JS : 파일의 분리

외부에서 사용할 경우

```javascript
Ext.requires('클래스명')
```

내부에서 사용할 경우

```javascript
requires:['클래스명']
```

## 컨테이너, 컴포넌트, 패널

<hr>

**✔ 컨테이너**

Ext JS는 많은 위젯들을 가지고 있다. 이러한 위젯은 자유롭게 추가하거나 제어할 수 있다. 이 경우 추가되는 위젯을 받을 상위 위젯이 필요한데 이러한 위젯을 컨테이너라고 한다. (위젯들이 담겨있는 공간)

**✔ 컴포넌트**

컴포넌트는 화면에 나타나는 모든 위젯을 말한다.

```javascript
// 컴포넌트
Ext.Button
// 다른 위젯을 포함 할 수 없음

// 컴포넌트이자 컨테이너
Ext.Panel
// 다른 위젯을 포함 할 수 있음
```

추가하는 방법은 컴포넌트를 xtype으로 정의하고 items에 추가한다.

```javascript
Ext.onReady(function(){
    Ext.create('Ext.paenl.Panel', {
    {
        ...
    }, html:['나는 컨테이너 입니다.','나는 컴포넌트를 포함하거나 다른 컨테이너 안에 들어갈 수 있습니다.'].join(""),
        items:[{
            xtype:'textareafield',
            value:'나는 컴포넌트입니다. 나는 컨테이너 안에 들어갑니다.'
        }]
    });
})
```
- items에 추가된 컴포넌트가 컨테이너 안에서 동작한다.
- 컨테이너가 컴포넌트를 추가하기 위한 방법으로 생성시 xtype을 이용하여 정적으로 처리하는 방법 이외에 필요할 경우 add 메소드를 이용하여 추가할 수 있다.

**✔ 패널**

패널은 가장 기본적인 화면을 보여주는 컨테이너이자 컴포넌트이다.

## 쿼리

<hr>

화면을 구성하는 위젯은 복잡하게 구성되어 있고 경우에 따라 필요로 하는 위젯을 찾아 설정해야 할 일이 발생한다.

query문 안의 형식은 일반적인 다른 자바스크립트 라이브러리와 비슷하다. Ext.ComponentQuery.query는 쿼리문에 해당하는 위젯을 가져온다. 여러건이 될 수 있으므로 하나의 위젯을 사용할 경우 항상 배열 형태의 인덱스 값을 추가하여 처리해야 한다.

```javascript
Ext.ComponentQuery.query('datefield')[0];

// name 속성이 추가되었을 경우
Ext.ComponentQuery.query('datefield[name=myDateField1]')[0];

// id기준 조회
Ext.getCmp('myDateFieldId');
// 혹은
Ext.ComponentQuery.query('#myDateFieldId')[0];
```
**✔ 쿼리문을 이용하여 자식노드 위젯, 부모노드 위젯, 자매노드 찾기**

```javascript
// 자식노드 위젯 찾기 1
// 공백 ' '을 사용한다.
Ext.ComponentQuery.query('panel fieldset')[0]

// 자식노드 위젯 찾기 2
// '>' 문자사용하기
Ext.ComponentQuery.query('panel>fieldset')[0]

// 자식노드 위젯 찾기 3
// down메소드 쓰기
위젯.down('fieldset datefield')

// 부모노드 위젯 찾기
// up메소드 쓰기
위젯.up('fieldset')

// 자매노드 찾기
// previousSibling or nextSibling 쓰기
위젯.previousSibling('[name=myDateField1]');
```

**✔ 상위 객체 나타나는 옵션 추가**

```javascript
Ext.ComponentQuery.query('datefield', panel)[0]

// 객체를 이용하여 query문만 이용하여 처리
panel.query('datefield', panel)[0];

// 여러위젯 동시 호출 (콤마 사용)
panel.query('datefield, testfield')[0];
```

## 이벤트

이벤트란 버튼이 클릭되거나 포커스를 갖거나 잃거나 화면에 위젯이 그려지거나 또는 사용자가 발생시키는 동작이다. 이벤트는 동적인 처리를 할 수 있으므로 위젯의 동작에 필요한 처리를 할 수 있다.

**✔ 이벤트를 처리하는 방법 2가지**

1. handler 이벤트 함수 부여하기
2. listeners를 추가하기

**✔ 이벤트 예시**

```javascript
{
    위젯
    listeners:[
        click:function(){
            ... (이벤트 처리)...
        }
    ]
}

// or
handler:function(){
    ...
}
```

**✔ listeners vs addListener**

listeners : 정적인 이벤트 선언 방법

addListener : 동적으로 이벤트를 추가하는 방식(on을 이용하여 추가할 수도 있음)

```javascript
위젯.addListen('이벤트명', function(){
    ...(이벤트 처리)...
});

// or
위젯.on('이벤트명', function(){
    ...(이벤트 처리)...
});
```

**✔ 델리게이트(Delegate)**

델리게이트(Delegate)는 상위 객체에 이벤트를 걸어놓는 방법으로 이벤트 대상을 필터링하여 제어할 수 있다.

```javascript
...
items:[{
    xtype:'button',
    name:'button1',
    text:확인
}],
listeners:[
    {
        delegate:'button[name=button1]'
        ...
    }
]
```

**✔ element를 이용한 이벤트 확장**

기본적으로 제공되지 않는 이벤트를 부여하려면 해당 위젯의 엘리먼트(element)를 사용할 수 있다. 엘리먼트의 이벤트를 받아 처리하려면 listeners에 el을 붙여 엘리먼트의 이벤트임을 정의할 수 있다.

```javascript
listeners:{
    change:function(){
        ...
    },
    el:{
        click:function(){
            console.log("datefield inclick', arguments);
        }
    }
}

// 날짜필드의 경우 클릭 이벤트를 받을 수 없으나 엘리먼트를 이용하여 클릭이벤트를 받을 수 있게 되었음

// 동적인 이벤트 추가하기
...
var dateField1=Ext.ComponentQuery.query)'datefield[name=myDateField1'][0];

// 1st method
dateField1.el.addListener('click', function(){
    ...
});

// 2nd method
dateField2.el.on('click', function(){
    ...
});
```

- **delegate는 element를 이용한 이벤트 제어를 할 수 없다.**