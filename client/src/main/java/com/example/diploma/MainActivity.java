package com.example.diploma;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.os.Handler;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.Spinner;
import android.widget.TextView;
import android.widget.Toast;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;

public class MainActivity extends AppCompatActivity {

    Socket s;
    DataOutputStream dos;
    PrintWriter pw;
    public static final int PORT = 8080;
    public static final String HOST = "192.168.0.104";
    private Button button;
    private Button button2;
    private TextView result;
    private String[] namesArr = new String[] {"Адыгея", "Алтай", "Амурская обл.","Архангельская обл.", "Астраханская обл.","Башкортостан", "Белгородская обл.","Брянская обл."
            , "Бурятия","Владимирская обл.", "Вологодская обл.","Дагестан", "Еврейская АО", "Ингушетия","Кабардино-Балкария", "Калмыкия","Карелия", "Краснодарский край",
            "Красноярский край", "Крым","Курганская обл.", "Ленинградская обл.","Москва", "Московская обл.", "Нижегородская обл.","Новгородская обл.",
            "Новосибирская обл.","Пермский край", "Псковская обл.","Ростовская обл.", "Самарская обл.","Санкт-Петербург", "Саха (Якутия)","Свердловская обл.",
            "Севастополь", "Татарстан","Томская обл.", "Тюменская обл.","ХМАО – Югра", "Хабаровский край","Хакасия", "Челябинская обл.","Чечня", "Ярославская обл."};

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


        ArrayAdapter<String> adapter = new ArrayAdapter<>(this, android.R.layout.simple_spinner_item, namesArr);
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);

        Spinner spCity = (Spinner) findViewById(R.id.spCity);
        spCity.setAdapter(adapter);

        button = findViewById(R.id.button);
        button2 = findViewById(R.id.button2);
        result = findViewById(R.id.result);

        button.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View view) {
                String text = spCity.getSelectedItem().toString();
                text = '1' + text;
                Sender sender = new Sender();
                sender.execute(text);

            }
        });

        button2.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View view) {
                String text = spCity.getSelectedItem().toString();
                text = '2' + text;
                Sender sender = new Sender();
                sender.execute(text);
            }
        });
    }

    public class Sender extends AsyncTask<String,String,String>
    {

        protected void onPreExecute(){
            super.onPreExecute();
            result.setText("Ожидайте...");
        }
        Socket s = null;
        PrintWriter writer;
        BufferedReader in;


        @Override
        public String doInBackground(String... strings) {

            try {
                    String text = strings[0];
                    s = new Socket(HOST, PORT);
                    writer = new PrintWriter(s.getOutputStream());
                    writer.write(text);
                    writer.flush();
                    in = new BufferedReader(new InputStreamReader(s.getInputStream()));
                    String serverWord = in.readLine(); // ждём, что скажет сервер
                    writer.close();
                    in.close();
                    s.close();
                    return serverWord;
            }

            catch (IOException e){
                e.printStackTrace();}
            return null;
        }
        @Override
        protected void onPostExecute(String serverWord){
            super.onPostExecute(serverWord);
            result.setText(serverWord);
        }
    }
}