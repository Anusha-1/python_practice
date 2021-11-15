import xml.dom.minidom

def main():
    doc=xml.dom.minidom.parse("mydata.xml")#DOM tree in memory
    print(doc.nodeName)
    print(doc.firstChild.tagName)

    expert = doc.getElementsByTagName('expertise')
    print(f"expert in {expert.length} skills")
    for skill in expert:
        print(skill.getAttribute("name"))
    
    newskill=doc.createElement("expertise")
    newskill.setAttribute("name","BigData")
    doc.firstChild.appendChild(newskill)
    print("new skill added....")

    print("After addning new skill ......")
    expert = doc.getElementsByTagName("expertise")
    print(f"expert in {expert.length} skills")
    for skill in expert:
        print(skill.getAttribute("name"))

main()
