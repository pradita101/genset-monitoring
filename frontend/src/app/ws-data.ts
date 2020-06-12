// export interface WsData {
//   Id: string; // id mesin
//   Dmy: string; // tanggal
//   Hms: string; // waktu GMT+7
//   Lat: number; // latitude
//   Long: number; // longitude
//   Tmp: number; // suhu 27.06 celcius
//   I: number; // arus 0.27 ampere
//   V: number; // voltase 0 volt
//   Eng: number; // mesin on (jika off, "Eng":"0")
//   Vbat: number; // ??? (tegangan aki (volt))
//   Pres: number; // tekanan 50 Pa (masih data dummy, untuk satuan belum pasti, menunggu sensor fix dahulu)
//   Lvl: number; // ???    (fuel level, masih data dummy)
//   Cons: number; // ???    (fuel consumption, masih data dummy)
//   Eh: string; // mesin sudah hidup selama 2 menit
//   Time: number;
// }

export interface WsData{
  A: string, //Device ID
  B: string, //Unix Time in Second
  C: Array<string>, //GPS Parameter Lat, Long, Heading, Speed
  D: string, //Time when Genset On in Second
  E: string, //Time when Genset Off in Second
  F: string, //Engine Hour
  G: string, //Room Temperature
  H: string, //Battery Voltage
  I: string, //Engine Status Bool(1/0, On/Off)
  J: Array<string>, //Current RST IR,IS,IT
  K: Array<string>, //Voltage RST VR,VS,VT
  L: Array<string>, //kVA RST kVAR,kVAS,kVAT
  M: string, //Tank Level on Litre
  N: string, //Fuel Consumption on Litre
  O: string, //Pressure Engine
  P: string, //RPM Engine
  Q: string, //Coolant Temperature
  R: string, //Firmware Version
  S: Array<string>, //Device Status Pin Status, Signal Quality, Network Mode, SDCard Status, Err1, Err2, Err3, Free Memory
  T: string, //Temporary output stream
  U: string, //Temporary Frequency
  V: string, //Temporary for genset mode
}

// export interface WsData{
//   "A":"DFXX", //Device ID
//   "B":"1576563163", //Unix Time in Second
//   "C":["-6.288","106.817","0.490","35.330"], //GPS Parameter Lat, Long, Heading, Speed
//   "D":"1576563131", //Time when Genset On in Second
//   "E":"1576563053", //Time when Genset Off in Second
//   "F":"131085", //Engine Hour
//   "G":"-127.00", //Room Temperature
//   "H":"0", //Battery Voltage
//   "I":"1", //Engine Status Bool(1/0, On/Off)
//   "J":["4.84","5.19","4.26"], //Current RST IR,IS,IT
//   "K":["0.00","0.00","0.00"], //Voltage RST VR,VS,VT
//   "L":["0.00","0.00","0.00"], //kVA RST kVAR,kVAS,kVAT
//   "M":"0.00", //Tank Level on Litre
//   "N":"0.00", //Fuel Consumption on Litre
//   "O":"0.00", //Pressure Engine
//   "P":"0.00", //RPM Engine
//   "Q":"0.00", //Coolant Temperature
//   "R":"SAJ-alpha", //Firmware Version
//   "S":["1","23,99","8","1","0","0","0","3593"] //Device Status Pin Status, Signal Quality, Network Mode, SDCard Status, Err1, Err2, Err3, Free Memory
// }
