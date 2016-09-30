#coding=utf-8
from jnius import autoclass,cast

'''
permission
  <uses-permission android:name="android.permission.CHANGE_NETWORK_STATE"></uses-permission>
  <uses-permission android:name="android.permission.CHANGE_WIFI_STATE"></uses-permission>
  <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"></uses-permission>
  <uses-permission android:name="android.permission.ACCESS_WIFI_STATE"></uses-permission>
  ACCESS_COARSE_LOCATION,ACCESS_FINE_LOCATION
'''
Context = autoclass('android.content.Context')
ConnectivityManager = autoclass('android.net.ConnectivityManager')
WifiConfiguration = autoclass('android.net.wifi.WifiConfiguration')
WifiManager = autoclass('android.net.wifi.WifiManager')
Activity = autoclass('android.app.Activity')

PythonActivity = autoclass('org.renpy.android.PythonActivity')
activity = PythonActivity.mActivity


#con_mgr = activity.getSystemService(Activity.CONNECTIVITY_SERVICE)
#conn = con_mgr.getNetworkInfo(ConnectivityManager.TYPE_WIFI).isConnectedOrConnecting()

WFM = activity.getSystemService(Context.WIFI_SERVICE)
WFM.startScan()

from kivy.app  import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.clock     import Clock
from kivy.core.window import Window

class MyApp(App):
	def build(self):
		self.mw=BoxLayout(orientation="vertical")
		#elf.mw.add_widget(Label(text='hehe'))
		#self.mw.add_widget(Label(text='haha'))
		self.sv=ScrollView()
		self.bx=BoxLayout(orientation='vertical',size_hint_y=None,height=0)
		self.sv.add_widget(self.bx)
		
		self.mw.add_widget(self.sv)
		
		self.ev1 = Clock.schedule_once(self.haha,1)
		self.iii = 0
		return self.mw
	def haha(self,*args):
		#self.mw.clear_widgets()
		#self.mw.add_widget(Label(text=WFI.getMacAddress()))
		rss=WFM.getScanResults()
		#self.iii+=1
		self.bx.clear_widgets()
		for ii in range(rss.size()):
			self.bx.add_widget(Label(size_hint_y=None,height=Window.height/16,text=str((rss.get(ii)).BSSID))) #Window
			self.bx.height+=Window.height/16
			self.bx.add_widget(Label(size_hint_y=None,height=Window.height/16,text=str((rss.get(ii)).SSID))) #Window
			self.bx.height+=Window.height/16
			self.bx.add_widget(Label(size_hint_y=None,height=Window.height/16,text=str((rss.get(ii)).level)))
			self.bx.height+=Window.height/16#rss.size() 	level SSID  ((rss.get(ii)).toString())[:20])
		#print 1
	def on_pause(self):
		return True
	def on_resume(self):
		return self.mw
		
if __name__=="__main__":
	MyApp().run()

	'''
Reference: 
	
	package com.app.wifi;
	 
	import java.util.List;
	import android.annotation.SuppressLint;
	import android.app.Activity;
	import android.content.BroadcastReceiver;
	import android.content.Context;
	import android.content.Intent;
	import android.content.IntentFilter;
	import android.net.wifi.ScanResult;
	import android.net.wifi.WifiManager;
	import android.os.Bundle;
	import android.widget.TextView;
	 
	public class CheckWifiNetworkActivity extends Activity {
	 
		private StringBuilder sb = new StringBuilder();
		private TextView tv;
		List<ScanResult> scanList;
	 
		@Override
		protected void onCreate(Bundle savedInstanceState) {
			super.onCreate(savedInstanceState);
			setContentView(R.layout.activity_main); 
			tv= (TextView)findViewById(R.id.txtWifiNetworks);
			getWifiNetworksList();
		}
	 
		private void getWifiNetworksList(){      
			IntentFilter filter = new IntentFilter();
			filter.addAction(WifiManager.SCAN_RESULTS_AVAILABLE_ACTION);
			final WifiManager wifiManager = 
					(WifiManager)getApplicationContext().getSystemService(Context.WIFI_SERVICE);;
					registerReceiver(new BroadcastReceiver(){
	 
						@SuppressLint("UseValueOf") @Override
						public void onReceive(Context context, Intent intent) {
							sb = new StringBuilder();
							scanList = wifiManager.getScanResults();
							sb.append("\n  Number Of Wifi connections :" + " " +scanList.size()+"\n\n");    
							for(int i = 0; i < scanList.size(); i++){
								sb.append(new Integer(i+1).toString() + ". ");
								sb.append((scanList.get(i)).toString());
								sb.append("\n\n");
							}
	 
							tv.setText(sb);  
						}
	 
					},filter);        
			wifiManager.startScan();
		}
	}

	WFM.startScan()
	#if d:
	WFM.getScanResults()

	please read android: why we should use activity.getSystemService(Activity.CONNECTIVITY_SERVICE) here
	Class that answers queries about the state of network connectivity. It also notifies applications when network connectivity changes. Get an instance of this class by calling Context.getSystemService(Context.CONNECTIVITY_SERVICE).

	Context = autoclass('android.content.Context')
	ConnectivityManager = autoclass('android.net.ConnectivityManager')
	WifiConfiguration = autoclass('android.net.wifi.WifiConfiguration')
	WifiManager = autoclass('android.net.wifi.WifiManager')
	Activity = autoclass('android.app.Activity')

	PythonActivity = autoclass('org.renpy.android.PythonActivity')
	activity = PythonActivity.mActivity

	#getScanResults()
	#wifi_conn = autoclass('android.net.wifi.WifiConfiguration')
	#wifi_man = autoclass('android.net.wifi.WifiManager')
	'''
