"use strict";

let hour = 0;
let minute = 0;
let second = 0;
let millisecond = 0;

let cron;

document.form_main.start.onclick = () => timer_calculation();
document.form_main.stop.onclick = () => stop();
document.form_main.pause.onclick = () => pause();
document.form_main.reset.onclick = () => reset();

function timer_calculation() {
  pause();
  cron = setInterval(() => { timer(); }, 10);
}

function pause() {
  clearInterval(cron);
}

function stop() {
  alert("You have to pay: " + calculation() + "€")
  clearInterval(cron);
  reset();
}

function reset() {
  hour = 0;
  minute = 0;
  second = 0;
  millisecond = 0;
  document.getElementById('hour').innerText = '00';
  document.getElementById('minute').innerText = '00';
  document.getElementById('second').innerText = '00';
  document.getElementById('millisecond').innerText = '000';
}

function timer() {
  if ((millisecond += 10) == 1000) {
    millisecond = 0;
    second++;
  }
  if (second == 60) {
    second = 0;
    minute++;
  }
  if (minute == 60) {
    minute = 0;
    hour++;
  }
  document.getElementById('hour').innerText = returnData(hour);
  document.getElementById('minute').innerText = returnData(minute);
  document.getElementById('second').innerText = returnData(second);
  document.getElementById('millisecond').innerText = returnData(millisecond);
}

function returnData(input) {
  return input > 10 ? input : `0${input}`
}

function calculation(){
        var usingTime = (hour * 60) + minute + (second / 60);
        var price = 0.30;
        var result = usingTime * price;
        return result.toFixed(2) ;
}
