import 'package:flutter/material.dart';

void main() {
  runApp(Myapp());
}

class Myapp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        backgroundColor: Colors.blue[848484],
        body: SafeArea(
          child: Column(
            //crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              CircleAvatar(
                radius: 70,
                backgroundImage:
                    AssetImage('images/LAVANDIERES-LOGO-OFFICIEL.png'),
              ),
              Text(
                'Lavandiére',
                style: TextStyle(
                  fontFamily: 'Pacifico',
                  fontSize: 40.0,
                  color: Colors.white,
                  fontWeight: FontWeight.bold,
                ),
              ),
              Container(
                child: Row(
                  children: [
                    FlatButton(
                        onPressed: () {

                        },
                        child: Text("Déja client"),
                      color: Colors.white,
                    )
                  ],
                ),
              ),
              Container(
                child: Row(
                  children: [
                    FlatButton(
                        onPressed: () {

                        },
                        child: Text("Commencer"),
                    color: Colors.white,
                    ),
                  ],
                ),
              ),
              Container(
                child: Row(
                  children: [
                    FlatButton(
                      onPressed: () {

                      },
                      child: Text("Commencent ca marche?"),
                      color: Colors.transparent,
                    ),
                  ],
                ),
              )
            ],
          ),
        ),
      ),
    );
  }
}
