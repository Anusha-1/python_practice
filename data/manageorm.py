from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ormdata import Address,Base,Person
engine=create_engine('sqlite:///boa.db')
Base.metadata.bind=engine

DBSession= sessionmaker(bind=engine) #unit of work(consistency)
session=DBSession()

#insert a new Person
new_person=Person(name="Anusha")
session.add(new_person)
session.commit()

new_address=Address(city='Hyderabad',post_code='500013',person=new_person)
session.add(new_address)
session.commit() # we need not do insert into , or select * , this is more professional
print("data inserted in tables")
