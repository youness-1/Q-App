package com.theapphideaway.addingpython

import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import com.chaquo.python.Python
import com.chaquo.python.android.AndroidPlatform
import kotlinx.android.synthetic.main.activity_main.*
import android.widget.Button
import java.text.SimpleDateFormat
import java.util.*


class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        if (! Python.isStarted()) {
            Python.start(AndroidPlatform(this))
        }
        val btnpd=findViewById(R.id.pd) as Button;
        val btndp=findViewById(R.id.dp) as Button;
        val py: Python = Python.getInstance()
        var pythonText = py.getModule("uni").callAttr("getdp", SimpleDateFormat("HH.mm", Locale.getDefault()).format(Date()))
        my_text_view.text = pythonText.toString()
        btnpd.setOnClickListener {
            pythonText = py.getModule("uni").callAttr("getpd", SimpleDateFormat("HH.mm", Locale.getDefault()).format(Date()))
            my_text_view.text = pythonText.toString()
        }
        btndp.setOnClickListener {
            pythonText = py.getModule("uni").callAttr("getdp", SimpleDateFormat("HH.mm", Locale.getDefault()).format(Date()))
            my_text_view.text = pythonText.toString()
        }
    }

}
