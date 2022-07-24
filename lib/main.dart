import 'dart:async';
import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import './screens/detail_screen.dart';

void main() => runApp(MaterialApp(
      home: MyApp(),
      routes: {
        DetailScreen.routeName: (ctx) => DetailScreen(),
      },
    ));

class MyApp extends StatefulWidget {
  @override
  _MyAppState createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  List data = [];

  Future<String> getData() async {
    var response = await http.get(
        Uri.encodeFull("http://10.0.2.2:5000/getstaff"),
        headers: {"Accept": "application/json"});

    this.setState(() {
      data = json.decode(response.body);
    });
    print(data[0]["userId"]);
    return "success";
  }

  @override
  void initState() {
    this.getData();
    super.initState();
  }

  void showStudent(ctx, i) {
    Navigator.of(ctx).pushNamed(DetailScreen.routeName, arguments: {
      "userId": data[i]["user_Id"].toString(),
      "referralCodeId": data[i]["referral_Code_Id"].toString(),
      "userName": data[i]["user_Name"].toString(),
      "role": data[i]["user_designation"].toString()
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.grey[800],
      appBar: AppBar(
        title: const Text('SecondFamilyDB'),
        backgroundColor: Colors.grey[850],
      ),
      body: Padding(
        padding: EdgeInsets.all(8.0),
        child: ListView.builder(
          itemCount: data.length == 0 ? 0 : data.length,
          itemBuilder: (ctx, i) => Column(
            children: <Widget>[
              GestureDetector(
                onTap: () => showStudent(context, i),
                child: Card(
                  color: Colors.grey[400],
                  child: ListTile(
                    title: Text(
                      "${data[i]["user_Id"]}",
                      style: TextStyle(fontSize: 20.0),
                    ),
                    subtitle: Text(
                      "${data[i]["user_designation"]}",
                      style: TextStyle(fontSize: 15.0),
                    ),
                    leading: CircleAvatar(
                      backgroundImage: AssetImage("assets/image/user.jpeg"),
                    ),
                  ),
                ),
              ),
              Divider()
            ],
          ),
        ),
      ),
    );
  }
}
