from flask import Flask,request,jsonify

app=Flask(__name__)
items=[
    {'id':1,'day':"monday",'name':"chest"},
    {'id':2,'day':"tuesday",'name':"wings"}
]

@app.route("/")
def home():
    return "welcome to the workouts to followed in gym"
@app.route("/items",methods=["GET"])
def getitems():
    return jsonify(items)

@app.route("/items/<int:item_id>",methods=["GET"])
def getitemsbyid(item_id):
    for item in items:
        if item["id"]==item_id:
            return jsonify(item)
    return jsonify({"error":"item not found"})

@app.route("/items",methods=["POST"])
def postitems():
    if not request.json:
        return jsonify({"error":"item not found"})
    new_items={
        'id':items[-1]["id"] + 1 if items else 1,
        'day':request.json['day'],
        'name':request.json['name']

    }
    items.append(new_items)
    return jsonify(items)

@app.route("/items/<int:item_id>",methods=["PUT"])
def updateitems(item_id):
    for item in items:
        if item["id"]==item_id:
            item['day']=request.json['day']
            item['name']=request.json['name']
            return jsonify(item)
    return jsonify({"error":"item not found"})
@app.route('/items/<int:item_id>',methods=["DELETE"])
def deleteitems(item_id):
    global items
    items=[item for item in items if item['id']!=item_id]
    return jsonify({"message":"item has been deleted"})


if __name__=="__main__":
    app.run(debug=True)