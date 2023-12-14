SLIP1.
Q2
1. Model the following Property system as a document database. Consider a
set of Property, Owner. One owner can buy many properties
>>>create database=durgesh
>use durgesh
2. Assume appropriate attributes and collections as per the query requirements.
>>db.createCollection(“owner”);
>>>db.createCollection(“propertys”);
>>show collection
3.Insert at least 05 documents in each collection.
>>db.product.insertMany([{“......”}]);
>>db.owner.insertMany([{.....”}]);
4. Answer the following Queries
a. Display area wise property details.
>>db.properties1.find({},{area:1,_id:101});
b. Display property owned by 'Mr.Patil' having minimum rate
>>db.Property.find({ ownerId: db.Owner.findOne({ name: "Mr. Patil" })._id }).sort({
. rate: 1 }).limit(1)
///this Query not correct— tula jml tr mala pn takkk………
c. Give the details of owner whose property is at “Nashik”.
>>db.owner.findOne({ "propertiesowned": { $in: [db.Property.findOne({ area: "Nashik"
. })]}});
………… OR……..
db.properties1.find({area:"Nashik"})
d. Display area of property whose rate is less than 100000.
>>db.properties1.find( { rate: { $gt:(100000)} } );







Json Format:Property collection
[
  {
    "_id": 1,
    "area": "Mumbai",
    "rate": 150000,
    "ownerId": 101
  },
  {
    "_id": 2,
    "area": "Pune",
    "rate": 120000,
    "ownerId": 102
  },
  {
    "_id": 3,
    "area": "Nashik",
    "rate": 90000,
    "ownerId": 103
  },
  // Add more property documents
]


----//-----------------------//------------------//-
Json format : Owner collection
[
  {
    "_id": 101,
    "name": "Mr. Patil",
    "propertiesOwned": [1, 4]  // Property IDs owned by Mr. Patil
  },
  {
    "_id": 102,
    "name": "Mrs. Shah",
    "propertiesOwned": [2, 5]
  },
  {
    "_id": 103,
    "name": "Mr. Deshmukh",
    "propertiesOwned": [3]
  },
  // Add more owner documents
]


