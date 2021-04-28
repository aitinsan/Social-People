import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Welcome to Flutter',
      home: Scaffold(
          appBar: AppBar(
            title: Text('Hello i am testing'),
          ),
          body: Column(
            children: [
              
              TitleSection(),
              BodySection(),
            ],
          )),
    );
  }

}
class TitleSection extends StatelessWidget {
  const TitleSection({Key key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(color: Colors.redAccent),
      width: 100,
      height: 100,
      child: Text("Hello world"),
    );
  }
}
class BodySection extends StatefulWidget {
  BodySection({Key key}) : super(key: key);

  @override
  _BodySectionState createState() => _BodySectionState();
}

class _BodySectionState extends State<BodySection> {
  @override
  Widget build(BuildContext context) {
    return Container(
       child: Text("this is body"),
    );
  }
}