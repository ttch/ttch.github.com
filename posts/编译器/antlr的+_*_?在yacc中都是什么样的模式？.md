#Antlr的+ * ?在yacc中都是什么样的模式？


因为正在完成的编译器 breed 需要把java项目转换到上面，所以需要对 Antlr的三种符号进行模式转换。


我们先看一下三种符号的作用

-  ( + ) 至少出现一次，至多不限制。
-  ( * ) 可能出现，也可能不出现。
-  ( ? ) 最多出现一次，也可能不出现。

就上面的三种种情况 看看ply中的yacc中怎么描述。

> +

Antlr
	
	annotations : (annotation)+ ;
	
yacc

    annotations : annotation
    			| annotations annotation
    			;

> *

Antlr

	annotationName : ID ('.' ID)* ;

yacc

	annotationName : ID ( IDS ) ;
	
	IDS : ID
		| IDS ‘.' ID
		| empty


> ?

Antlr

	classDeclaration
 	
	: 'class' ID (typeParameters)? ('extends' type)?
 	
	('implements' typeList)?
 	
	classBody
 	
	;

yacc
//我们假设yacc支持()吧！  要不得拆分出好多

	classDeclaration : 'class' ID 
				(typeParameters ) ('extends' type) ('implements' typeList)		classBody ;
	| 'class' ID 					('extends' type) 							classBody ;
	| 'class' ID	(typeParameters )  											classBody ;
	| 'class' ID									 ('implements' typeList)	classBody ;
	| 'class' ID (typeParameters ) ('extends' type) 							 classBody ;
	| 'class' ID 					('extends' type) ('implements' typeList)	classBody ;
	| 'class' ID (typeParameters )					 ('implements' typeList)	classBody ;
	
antlr使用正则的3种模式大量的节约了思考周期和代码的长度