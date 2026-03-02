import express from "express";
import admin from "./firebaseAdmin.js";
import cron from "node-cron";
import {User} from "../model/user.model.js"; 


// Function to send notification
async function sendNotification(token, title, body) {
  const message = {
      token,
    notification: { title, body },
  
  };
  try {
    await admin.messaging().send(message);
    console.log("✅ Notification sent to", token);
  } catch (err) {
    console.error("❌ Error sending notification:", err);
  }
}

// Schedule cron job every minute to check reminders
const sendnoti=()=>{
    cron.schedule("* * * * *", async () => {
  const now = new Date();
  const users = await User.find();
  for (const user of users) {
    // Compare current time with reminder time (within 1 minute)
    const medicineTime = new Date(user.time);
    if (
      Math.abs(medicineTime.getTime() - now.getTime()) < 60000 &&
      user.fcmToken
    ) {
      await sendNotification(
        user.fcmToken,
        "Medicine Reminder 💊",
        `Time to take ${user.medicine}`
      );
    }
  }
});
}
export {sendnoti};