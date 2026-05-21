#json flattening means converting the nested json into flat structure, all values at one level.
#example

data={
  "id": 1,
  "details": {
    "name": "Pranathi",
    "salary": 3000000
  }
}

#output {id:'1','name':'Pranathi','salary':3000000}
data_1={}

for key,value in data['details'].items():
    data_1['id']=data['id']
    data_1[key]=value
print(data_1)

orders={
  "order_id": 101,
  "customer": {
    "name": "Pranathi",
    "city": "Hyderabad"
  },
  "payment": {
    "method": "UPI",
    "amount": 2500
  }
}

flat={}

for order in orders:
    if isinstance(orders[order],dict):
        for key,value in orders[order].items():
            temp=order+'_'+key
            flat[temp]=value
    else:
        flat[order]=orders[order]
print(flat)  #this is without functions