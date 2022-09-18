## Ext JS API

**✔ [Sencha 공식 홈페이지](https://www.sencha.com/)**


**✔ [Sencha Documentation](https://docs.sencha.com/)**

### Ext JS

<hr>

**1. xtype**

각 컴포넌트는 xtype을 이용하여 정의한다.

```javascript
{
    xtype:'textfield',
    fieldLabel:'이름'
}
```

[Ext.Component xtype:component :: xtype:String](https://docs.sencha.com/extjs/7.5.1/modern/Ext.Component.html#cfg-xtype)

The xtype configuration option can be used to optimize Component creation and rendering. It serves as a shortcut to the full component name. For example, the component Ext.button.Button has an xtype of button.

You can define your own xtype on a custom Ext.Component like so:

**2. cls**

[Ext.Component xtype:component, box :: cls : String/String[]](https://docs.sencha.com/extjs/7.5.1/classic/Ext.Component.html#cfg-cls)

An optional extra CSS class that will be added to this component's Element. The value can be a string, a list of strings separated by spaces, or an array of strings. This can be useful for adding customized styles to the component or any of its children using standard CSS rules.


**3. items**

```javascript
items:[
    xtype:'textareafield',
    value:'나는 컴포넌트입니다. 나는 컨테이너 안에 들어갑니다.'
]
```

[Ext.Container xtype:container :: items:Array/Object](https://docs.sencha.com/extjs/7.5.1/modern/Ext.Container.html#cfg-items)

The child items to add to this Container. This is usually an array of Component configurations or instance

**4. reference**

[Ext.Component xtype:component, box :: reference : String](https://docs.sencha.com/extjs/7.5.1/classic/Ext.Component.html#cfg-reference)

Specifies a name for this component inside its component hierarchy. This name must be unique within its [view](https://docs.sencha.com/extjs/7.5.1/classic/Ext.container.Container.html#cfg-referenceHolder) or its [Ext.app.ViewController](https://docs.sencha.com/extjs/7.5.1/classic/Ext.app.ViewController.html). See the documentation in [Ext.container.Container](https://docs.sencha.com/extjs/7.5.1/classic/Ext.container.Container.html) for more information about references.

Note: Valid identifiers start with a letter or underscore and are followed by zero or more additional letters, underscores or digits. References are case sensitive.

**5. listeners**

[Ext.Component xtype:component, box :: listeners : Object](https://docs.sencha.com/extjs/7.5.1/classic/Ext.Component.html#cfg-listeners)

A config object containing one or more event handlers to be added to this object during initialization. This should be a valid listeners config object as specified in the [addListener](https://docs.sencha.com/extjs/7.5.1/classic/Ext.util.Observable.html#method-addListener) example for attaching multiple handlers at once.

DOM events from Ext JS [Ext.Component](https://docs.sencha.com/extjs/7.5.1/classic/Ext.Component.html)

While some Ext JS Component classes export selected DOM events (e.g. "click", "mouseover" etc), this is usually only done when extra value can be added.

**6. select**

[Ext SINGLETON :: (selector, composite) : Ext.dom.CompositeElementLit/Ext.dom.CompositeElement](https://docs.sencha.com/extjs/7.5.1/modern/Ext.html#method-select)

Shorthand for [Ext.dom.Element.select](https://docs.sencha.com/extjs/7.5.1/modern/Ext.dom.Element.html#method-select)

Selects descendant elements of this element based on the passed CSS selector to enable [Ext.dom.Element](https://docs.sencha.com/extjs/7.5.1/modern/Ext.dom.Element.html) methods to be applied to many related elements in one statement through the returned [Ext.dom.CompositeElementLite](https://docs.sencha.com/extjs/7.5.1/modern/Ext.dom.CompositeElementLite.html) object.

PARAMETERS

- selector :  String/HTMLElement[]

The CSS selector or an array of elements

- composite :  Boolean

Return a CompositeElement as opposed to a CompositeElementLite. Defaults to false.

RETURNS :Ext.dom.CompositeElementLite/Ext.dom.CompositeElement

**7. flex**

[Ext.Component xtype:component, box :: flex : Number](https://docs.sencha.com/extjs/7.5.1/classic/Ext.Component.html#cfg-flex)

Flex may be applied to child items of a box layout ([Ext.layout.container.VBox](https://docs.sencha.com/extjs/7.5.1/classic/Ext.layout.container.VBox.html) or [Ext.layout.container.HBox](https://docs.sencha.com/extjs/7.5.1/classic/Ext.layout.container.HBox.html)). Each child item with a flex property will fill space (horizontally in hbox, vertically in vbox) according to that item's relative flex value compared to the sum of all items with a flex value specified.

Any child items that have either a flex of 0 or undefined will not be 'flexed' (the initial size will not be changed).

**8. editable**

[Ext.field.ComboBox xtype:combobox, comboboxfield :: editable : Boolean](https://docs.sencha.com/extjs/7.5.1/modern/Ext.field.ComboBox.html#cfg-editable)

Configure as false to prevent the user from typing text directly into the field; the field can only have its value set programmatically or via an action invoked by a trigger.

Contrast with readOnly which disables all mutation via the UI.

Defaults to:

true

**9. increment**

[Ext.picker.Time xtype:timepicker :: increment : Number](https://docs.sencha.com/extjs/7.5.1/classic/Ext.picker.Time.html#cfg-increment)

The number of minutes between each time value in the list.

Defaults to:

15

