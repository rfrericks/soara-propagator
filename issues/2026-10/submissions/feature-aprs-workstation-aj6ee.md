---
section: "Member Feature"
author: "Kevin Brouelette, AJ6EE"
callsign: "AJ6EE"
issue: "October 2026"
submitted: "2026-09-29"
source: "submissions/_inbox/from-kevin-aj6ee-APRS_Keyboard_Messaging_PinPoint_Digirig_FTM-6000.pdf"
---

# Keyboard APRS Messaging: PinPoint APRS + Digirig + Soundmodem on a Yaesu FTM-6000

*By Kevin Brouelette, AJ6EE*

### Why this setup?

APRS is more than dots on a map. It is also a way to send short text messages over the air, station to station or to a whole group, without cell service or the internet. That makes it a useful tool for both emergency and non-emergency events: public service events, drills, hikes, and any time a short written message is clearer than a voice call.

Most licensed hams already own something with APRS capability, but many have never used it for messaging. Part of the reason is that typing a message one letter at a time on a radio keypad is slow. A computer changes that. With a full keyboard and screen you can send clear, complete messages quickly, read everything that comes in, and keep a record of it all.

This article shows how I set up a computer-based APRS messaging station using a Yaesu FTM-6000, a Digirig interface, and two free Windows programs: Soundmodem and PinPoint APRS.

### How the pieces fit together

| Yaesu FTM-6000 | → | Digirig | → | Soundmodem | → | PinPoint APRS |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 2 m / 70 cm radio | 10-pin DATA cable | audio + PTT | USB | software TNC | KISS TCP :8100 | map + messages |

**The radio.** The FTM-6000 is a solid 2 m/70 cm mobile with a data port on the back, but it has no APRS capability built in: no TNC, no message screen, no beaconing. This setup turns it into a full APRS messaging station with a real keyboard. The same approach works with almost any radio that has a data port, so many members can do this with a rig they already own.

**The Digirig.** The Digirig is a small USB interface that sits between the radio's data port and the computer. It lets PinPoint APRS hear APRS packets coming from the radio, send APRS packets back to the radio, and key the radio to transmit when a message or beacon needs to go out. One USB cable to the computer and one cable to the radio is the whole hardware setup.

**Soundmodem.** Soundmodem (free for Windows, by UZ7HO) is the software that connects the Digirig to PinPoint APRS. It acts as the TNC: it turns the packet tones heard through the Digirig into data PinPoint can read, and turns PinPoint's outgoing messages into tones for the radio to transmit. It runs quietly in the background, and PinPoint connects to it using KISS.

**PinPoint APRS.** PinPoint is the part you actually use: the map, the station list, and the message window.

### What you need

- Radio: Yaesu FTM-6000 (any radio with a data port works with the matching cable).
- Digirig Mobile USB audio/PTT interface. The USB-A to USB-C cable comes in the box.
- Digirig Yaesu FTM Mini-DIN-10 cable, 1200 baud version. It has a 10-pin mini-DIN plug for the radio on one end and two 3.5 mm plugs for the Digirig on the other.
- A Windows computer, laptop or desktop.
- Software (all free): Soundmodem, PinPoint APRS, and the Silicon Labs CP210x driver. Links are in the Resources section at the end.

### Connecting it

1. Install the CP210x driver on the computer. It gives Windows the COM port the Digirig uses for PTT.
2. Plug the 10-pin mini-DIN end of the cable into the DATA jack on the back of the FTM-6000.
3. Plug the two 3.5 mm plugs into the Digirig: green goes to the serial (PTT) port and black goes to the audio port.
4. Connect the Digirig to the computer with the included USB cable.
5. In Windows Device Manager, look under Ports (COM & LPT) for the new COM port and note the number. You will need it for Soundmodem.

### Radio setup (FTM-6000)

- Tune the radio to 144.390 MHz, the North American APRS frequency.
- Set Menu 16 PKT.SPD to 1200BP: press and hold [F menu], turn the DIAL to 16 PKT.SPD, press the DIAL, select 1200BP, and press to confirm.
- Turn off Dual Watch and scanning so the radio stays on 144.390.
- Open the squelch (turn it all the way off). Soundmodem does its own detection, and an open squelch keeps the radio from cutting off the start or end of a packet. The radio's volume knob only sets the speaker level and does not affect the audio going to the Digirig, so set it wherever is comfortable (or all the way down for a quiet station).

> **Important:** the FTM-6000's PKT.SPD setting defaults to 9600BP from the factory. APRS runs at 1200 baud, so this has to be changed or nothing will decode.

### Setting up Soundmodem

Soundmodem has two settings screens, Settings → Devices and Settings → Modems.

**Devices screen**

- Output / Input device: choose Speakers (USB Audio Device) and Microphone (USB Audio Device). That is the Digirig.
- Sample rates: leave TX and RX at 11025.
- Single channel output: checked. Dual channel: unchecked.
- KISS Server Port: 8100, Enabled. This is the port PinPoint APRS connects to.
- AGWPE Server Port: not needed; leave it unchecked.
- PTT Port: the Digirig's COM port (COM4 on my computer). Yours will probably be different; use the number you found in Device Manager.

**Modems screen**

- Channel A mode: AFSK AX.25 1200bd, standard APRS.
- TXDelay: 250 ms. TXTail: 50 ms.
- Leave the filters on Default settings. Channel B is ignored in single channel mode.

![Soundmodem Settings → Devices](assets/feature-aprs-soundmodem-devices-aj6ee-01.png){: style="height:3.2in; width:auto"} ![Soundmodem Settings → Modems](assets/feature-aprs-soundmodem-modems-aj6ee-02.png){: style="height:3.2in; width:auto"}

*Soundmodem Settings → Devices (left) and Settings → Modems (right). Screenshots by Kevin Brouelette, AJ6EE.*

**Main window**

Check that channel A shows AFSK AX.25 1200bd and the center frequency is 1700 Hz (the arrows below). When the radio hears APRS traffic, packets scroll by in the main window and the tones appear on the waterfall at the bottom. That is your first sign the radio, Digirig and Soundmodem are all working together.

![Soundmodem main window decoding live APRS traffic](assets/feature-aprs-soundmodem-main-aj6ee-03.png)

*Soundmodem main window decoding live APRS traffic. Screenshot by Kevin Brouelette, AJ6EE.*

> **Tip:** plugging in the Digirig can make Windows switch its default sound device to it. Set your computer's normal speakers back as the default playback device, or Windows sounds (notifications, beeps) may end up transmitted over the air.

### Setting up PinPoint APRS

Open Tools → Options.

**TNC tab**

- TNC type: network KISS mode.
- Connect TNC automatically when PinPoint APRS starts: checked.
- TCP/IP address: 127.0.0.1 ("this computer," since Soundmodem runs on the same machine).
- Port: 8100. It must match Soundmodem's KISS port.
- Ignore the Serial TNC Settings section; it is only used with a hardware TNC.

![PinPoint APRS Options → TNC tab](assets/feature-aprs-pinpoint-tnc-tab-aj6ee-04.png)

*PinPoint APRS Options → TNC tab. Screenshot by Kevin Brouelette, AJ6EE.*

**APRS tab**

- My APRS Call sign + SSID: your callsign with an SSID (I use AJ6EE-1).
- APRS path: WIDE1-1,WIDE2-1.
- Position comment: optional short text sent with your beacon.
- Station icon: any icon you like.
- Enable APRS beaconing: checked. For a fixed station, a long interval such as 360 minutes (6 hours) keeps you on the map without adding traffic to the channel.
- Use RF (Radio): checked. Use APRS-IS (Internet): unchecked. Everything goes over the air, which is the point for emergency use.
- APRS DigiPeater: leave it off.

![PinPoint APRS Options → APRS tab](assets/feature-aprs-pinpoint-aprs-tab-aj6ee-05.png)

*PinPoint APRS Options → APRS tab. Screenshot by Kevin Brouelette, AJ6EE.*

**Main screen**

The status bar at the bottom shows whether everything is connected. Look for TNC Connected and Beaconing Enabled. Stations heard on the air appear on the map, and new messages are counted in the status bar.

![PinPoint APRS main screen](assets/feature-aprs-pinpoint-main-aj6ee-06.png)

*PinPoint APRS main screen: stations heard over RF, with TNC Connected in the status bar. Screenshot by Kevin Brouelette, AJ6EE.*

### Using PinPoint APRS

- **F1:** beacon now. Transmits your position immediately. A good first test: watch Soundmodem or listen to the radio to confirm it transmits.
- **F10:** Messages window. Where you read and send APRS messages.
- **View → Communications:** opens the Communications Monitor, a live view of received APRS traffic.

**Sending and reading messages (F10)**

The Messages window works much like an email program:

- Folders on the left: Inbox (with Bulletins), Sent, Drafts and Deleted Items.
- New starts a message. Enter the destination and your text, then send it.
- Reply answers the selected message. Re-send sends one again if it was not acknowledged.
- Reading Pane shows the full text of the selected message at the bottom.

Your Sent folder keeps a time-stamped record of every message, which is useful for logging during an event.

![PinPoint APRS Messages window](assets/feature-aprs-pinpoint-messages-aj6ee-07.png)

*PinPoint APRS Messages window (Sent folder) showing messages to stations, CQ and the CLARA group. Screenshot by Kevin Brouelette, AJ6EE.*

**Communications Monitor**

This window shows the same live traffic as Soundmodem's monitor, but it is easier to read: one line per packet, each with a timestamp. It also has Save Data to keep a log, which is handy after an event.

![PinPoint Communications Monitor next to Soundmodem's monitor](assets/feature-aprs-comm-monitor-aj6ee-08.png)

*PinPoint's Communications Monitor (left) next to Soundmodem's monitor (right): same traffic, cleaner layout. Screenshot by Kevin Brouelette, AJ6EE.*

### APRS groups

An APRS message is addressed to a name of up to nine characters. Usually that name is a callsign with SSID, such as KN6PHW or AJ6EE-2, and the message goes to that one station. But the address does not have to be a callsign. It can be a group name, and any station set up to watch for that name will show the message.

That is what makes groups useful for events. Instead of sending the same message to five people one at a time, you send it once to the group, and everyone on the team sees it.

**Built-in and custom groups**

- Yaesu APRS radios come with ALL, CQ, QST and YAESU preset as group codes, with empty slots for your own. Other brands have similar group or bulletin settings.
- CQ is the general "anyone listening?" group, and a good way to say hello on APRS.
- A custom group is any name your group agrees on, for example CLARA. Each member adds it to an empty group slot on their radio. In PinPoint, simply enter the group name as the destination.

**Tips for using groups**

- Agree on the name ahead of time and have everyone add it before the event. Keep it short, unique, and no more than nine characters.
- Group messages are generally not acknowledged the way station-to-station messages are. For anything important, ask for a reply or send it directly to the station who needs it.
- Keep messages short. 144.390 is a shared channel, so avoid repeating messages rapidly.
- Bulletins (sent to BLN addresses) show up in PinPoint's Bulletins folder and are useful for announcements to everyone in range.

### Quick troubleshooting

| Symptom | Check |
|---|---|
| No COM port for the Digirig | Install the CP210x driver, then unplug and replug the Digirig. |
| Nothing decodes in Soundmodem | Radio on 144.390? PKT.SPD set to 1200BP? Input device set to the USB Audio Device? |
| Radio will not transmit | Soundmodem PTT Port matches the Digirig COM port; green plug is in the serial port. |
| PinPoint says TNC disconnected | Soundmodem is running; KISS port is 8100 in both programs; address is 127.0.0.1. |
| Windows sounds going out on the air | Set the computer's own speakers back as the default playback device. |

### Resources

- PinPoint APRS: free APRS client for Windows (map, messaging, station list). [pinpointaprs.com](https://www.pinpointaprs.com)
- Soundmodem (UZ7HO): free software TNC for Windows. [uz7.ho.ua/packetradio.htm](http://uz7.ho.ua/packetradio.htm)
- Digirig: audio/PTT interface and radio-specific cables. [digirig.net](https://digirig.net)
- Digirig Yaesu FTM Mini-DIN-10 cable (1200 baud version). [digirig.net/product/yaesu-ftm-cable](https://digirig.net/product/yaesu-ftm-cable)
- Silicon Labs CP210x USB-to-UART driver: provides the Digirig's COM port for PTT. silabs.com, USB-to-UART VCP drivers

73, AJ6EE

## Editor Notes

- **AI-assisted:** Kevin's cover note says he "had Claude put this document together" from his screenshots and description. Ray should decide on final inclusion and whether to add a disclosure line (e.g., "Prepared with AI assistance").
- Text extracted from Kevin's 8-page PDF in full; nothing cut or reworded. PDF page footers dropped. The page-1 block diagram (vector art) is reproduced as a simple table with the same labels; all 8 screenshots included (Devices/Modems shown side by side as in the original).
- Byline expanded from "by AJ6EE" to his name from the email; sign-off "73, AJ6EE" kept.
- Resource links made clickable; verify they resolve. The silabs.com entry had no specific URL, left as text.
- "CLARA" group and callsigns KN6PHW/AJ6EE-2 are Kevin's examples; not verified.
- Long article (~4–5 printed pages). Per CLAUDE.md, run in full.
