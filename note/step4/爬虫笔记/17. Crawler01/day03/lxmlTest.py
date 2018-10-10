# -*- coding: utf-8 -*-
"""
Created on Wed May 23 11:17:34 2018

@author: Administrator
"""

from lxml import etree

xml = """<bookstore>
<book>
	<title lang="en">Harry Potter</title>
	<author>J K. Rowling</author>
	<year>2005</year>
	<price>29.95</price>
</book>
<book>
	<title lang="chs">Python爬虫</title>
	<author>Joe</author>
	<year>2018</year>
	<price>39.95</price>
</book>
</bookstore>
"""


def info(object, spacing=10, collapse=0):
    """
    打印object中可以被调用的方法的信息
    """
    methodList = [method for method in dir(object) 
                  if callable(getattr(object, method))]
     
    # collapse是一个开关： 1表示打开紧凑的效果；0维持原样显示；
    processFun = collapse and (lambda s:"".join(s.split())) or (lambda s:s)
    
    print('\n'.join(["%s %s"%(str(method.ljust(spacing)), 
                              processFun(str(getattr(object, method).__doc__))) 
                              for method in methodList] ))

# 根节点
root = etree.fromstring(xml)
#print(root)

# book子节点
elements = root.xpath('book')
#print(elements)
#[<Element book at 0xa6771c8>, <Element book at 0xa677248>]
#print(elements[0])
#info(elements[0])
#print(elements[0].getchildren()[0].text)
       
# 尝试用不关心节点结构的方法来获取到数据
attributesElements = root.xpath("//@lang")
#print(attributesElements)
#['en', 'chs']

elements = root.xpath("/bookstore/book[price>20]/title")
#for it in elements:
#    print(it.text)


elements = root.xpath("/bookstore/book/title[@lang='chs']")
for it in elements:
    print(it.text)

 
#addnext    addnext(self, element)
#
#        Adds the element as a following sibling directly after this
#        element.
#
#        This is normally used to set a processing instruction or comment after
#        the root node of a document.  Note that tail text is automatically
#        discarded when adding at the root level.
#        
#addprevious addprevious(self, element)
#
#        Adds the element as a preceding sibling directly before this
#        element.
#
#        This is normally used to set a processing instruction or comment
#        before the root node of a document.  Note that tail text is
#        automatically discarded when adding at the root level.
#        
#append     append(self, element)
#
#        Adds a subelement to the end of this element.
#        
#clear      clear(self)
#
#        Resets an element.  This function removes all subelements, clears
#        all attributes and sets the text and tail properties to None.
#        
#cssselect  
#        Run the CSS expression on this element and its children,
#        returning a list of the results.
#
#        Equivalent to lxml.cssselect.CSSSelect(expr)(self) -- note
#        that pre-compiling the expression can provide a substantial
#        speedup.
#        
#extend     extend(self, elements)
#
#        Extends the current children by the elements in the iterable.
#        
#find       find(self, path, namespaces=None)
#
#        Finds the first matching subelement, by tag name or path.
#
#        The optional ``namespaces`` argument accepts a
#        prefix-to-namespace mapping that allows the usage of XPath
#        prefixes in the path expression.
#        
#findall    findall(self, path, namespaces=None)
#
#        Finds all matching subelements, by tag name or path.
#
#        The optional ``namespaces`` argument accepts a
#        prefix-to-namespace mapping that allows the usage of XPath
#        prefixes in the path expression.
#        
#findtext   findtext(self, path, default=None, namespaces=None)
#
#        Finds text for the first matching subelement, by tag name or path.
#
#        The optional ``namespaces`` argument accepts a
#        prefix-to-namespace mapping that allows the usage of XPath
#        prefixes in the path expression.
#        
#get        get(self, key, default=None)
#
#        Gets an element attribute.
#        
#getchildren getchildren(self)
#
#        Returns all direct children.  The elements are returned in document
#        order.
#
#        :deprecated: Note that this method has been deprecated as of
#          ElementTree 1.3 and lxml 2.0.  New code should use
#          ``list(element)`` or simply iterate over elements.
#        
#getiterator getiterator(self, tag=None, *tags)
#
#        Returns a sequence or iterator of all elements in the subtree in
#        document order (depth first pre-order), starting with this
#        element.
#
#        Can be restricted to find only elements with a specific tag,
#        see `iter`.
#
#        :deprecated: Note that this method is deprecated as of
#          ElementTree 1.3 and lxml 2.0.  It returns an iterator in
#          lxml, which diverges from the original ElementTree
#          behaviour.  If you want an efficient iterator, use the
#          ``element.iter()`` method instead.  You should only use this
#          method in new code if you require backwards compatibility
#          with older versions of lxml or ElementTree.
#        
#getnext    getnext(self)
#
#        Returns the following sibling of this element or None.
#        
#getparent  getparent(self)
#
#        Returns the parent of this element or None for the root element.
#        
#getprevious getprevious(self)
#
#        Returns the preceding sibling of this element or None.
#        
#getroottree getroottree(self)
#
#        Return an ElementTree for the root node of the document that
#        contains this element.
#
#        This is the same as following element.getparent() up the tree until it
#        returns None (for the root element) and then build an ElementTree for
#        the last parent that was returned.
#index      index(self, child, start=None, stop=None)
#
#        Find the position of the child within the parent.
#
#        This method is not part of the original ElementTree API.
#        
#insert     insert(self, index, element)
#
#        Inserts a subelement at the given position in this element
#        
#items      items(self)
#
#        Gets element attributes, as a sequence. The attributes are returned in
#        an arbitrary order.
#        
#iter       iter(self, tag=None, *tags)
#
#        Iterate over all elements in the subtree in document order (depth
#        first pre-order), starting with this element.
#
#        Can be restricted to find only elements with a specific tag:
#        pass ``"{ns}localname"`` as tag. Either or both of ``ns`` and
#        ``localname`` can be ``*`` for a wildcard; ``ns`` can be empty
#        for no namespace. ``"localname"`` is equivalent to ``"{}localname"``
#        (i.e. no namespace) but ``"*"`` is ``"{*}*"`` (any or no namespace),
#        not ``"{}*"``.
#
#        You can also pass the Element, Comment, ProcessingInstruction and
#        Entity factory functions to look only for the specific element type.
#
#        Passing more than one tag will let the iterator return all elements
#        matching any of these tags, in document order.
#        
#iterancestors iterancestors(self, tag=None, *tags)
#
#        Iterate over the ancestors of this element (from parent to parent).
#
#        Can be restricted to find only elements with a specific tag,
#        see `iter`.
#        
#iterchildren iterchildren(self, tag=None, *tags, reversed=False)
#
#        Iterate over the children of this element.
#
#        As opposed to using normal iteration on this element, the returned
#        elements can be reversed with the 'reversed' keyword and restricted
#        to find only elements with a specific tag, see `iter`.
#        
#iterdescendants iterdescendants(self, tag=None, *tags)
#
#        Iterate over the descendants of this element in document order.
#
#        As opposed to ``el.iter()``, this iterator does not yield the element
#        itself.  The returned elements can be restricted to find only elements
#        with a specific tag, see `iter`.
#        
#iterfind   iterfind(self, path, namespaces=None)
#
#        Iterates over all matching subelements, by tag name or path.
#
#        The optional ``namespaces`` argument accepts a
#        prefix-to-namespace mapping that allows the usage of XPath
#        prefixes in the path expression.
#        
#itersiblings itersiblings(self, tag=None, *tags, preceding=False)
#
#        Iterate over the following or preceding siblings of this element.
#
#        The direction is determined by the 'preceding' keyword which
#        defaults to False, i.e. forward iteration over the following
#        siblings.  When True, the iterator yields the preceding
#        siblings in reverse document order, i.e. starting right before
#        the current element and going backwards.
#
#        Can be restricted to find only elements with a specific tag,
#        see `iter`.
#        
#itertext   itertext(self, tag=None, *tags, with_tail=True)
#
#        Iterates over the text content of a subtree.
#
#        You can pass a tag name to restrict text content to specific elements,
#        see `iter`.
#
#        You can set the ``with_tail`` keyword argument to ``False`` to skip
#        over tail text.
#        
#keys       keys(self)
#
#        Gets a list of attribute names.  The names are returned in an
#        arbitrary order (just like for an ordinary Python dictionary).
#        
#makeelement makeelement(self, _tag, attrib=None, nsmap=None, **_extra)
#
#        Creates a new element associated with the same document.
#        
#remove     remove(self, element)
#
#        Removes a matching subelement. Unlike the find methods, this
#        method compares elements based on identity, not on tag value
#        or contents.
#        
#replace    replace(self, old_element, new_element)
#
#        Replaces a subelement with the element passed as second argument.
#        
#set        set(self, key, value)
#
#        Sets an element attribute.
#        
#values     values(self)
#
#        Gets element attribute values as a sequence of strings.  The
#        attributes are returned in an arbitrary order.
#        
#xpath      xpath(self, _path, namespaces=None, extensions=None, smart_strings=True, **_variables)
#
#        Evaluate an xpath expression using the element as context node.

