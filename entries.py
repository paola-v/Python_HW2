from main import db, Dog, Owner

#CREATE 2 DOG ENTRIES
spike = Dog('Spike','Shih Tzu',4,'girl')
reksy = Dog('Reksy','German Shepherd',6,'boy')

#ADD DOGS TO THE DB
db.session.add_all([spike,reksy])
db.session.commit()

#CHECK
print(Dog.query.all())
spike = Dog.query.filter_by(name='Spike').first()
reksy = Dog.query.filter_by(name='Reksy').first()

#CREATE 2 OWNERS
daniella = Owner('Daniella',spike.id)
james = Owner('James',reksy.id)

#ADD DOG OWNERS TO THE DB
db.session.add_all([daniella,james])
db.session.commit()


#CHECK
spike = Dog.query.filter_by(name='Spike').first()
print(spike)