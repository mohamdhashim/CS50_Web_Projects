document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);
  document.querySelector('#compose-form').addEventListener("submit",send_email);
  // By default, load the inbox


  load_mailbox('inbox');
});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = 'mega man';
}

function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';


  // Show the mailbox name
  document.querySelector('#maillist').innerHTML = ''

  if (mailbox == 'sent'){


    // receive the sent data from the server
    fetch('/emails/sent')
      .then(response => response.json())
      .then(emails => {
        // Print result
        emails.forEach(email => {
          mail_list(email.archived,email.recipients,email.subject,timestamp(email.timestamp))
        });  
    });

    
  }else if(mailbox == "inbox"){
          // receive the sent data from the server
    fetch('/emails/inbox')
    .then(response => response.json())
    .then(emails => {
      // Print result
      emails.forEach(email => {
        mail_list(email.read,email.sender,email.subject,timestamp(email.timestamp))
      });  
  });
  }else if(mailbox == "archived")
  {
    i = 3
    fetch('/emails/inbox')
    .then(response => response.json())
    .then(emails =>{
      emails.forEach(email =>{
        if (email.archived)
          mail_list(email.read,email.sender,email.subject,timestamp(email.timestamp),i)
          i++
      })
    })

  }

}
function timestamp(date){ //to fromat how timestamp of mail will be presented
  
  let today = new Date();
  today = today.toDateString();
  today = today.split(' ');

  date = date.split(' ');
  if(today[3]+',' != date[2]){ //year not equal current year
    return (`${date[0]} ${date[1]} ${date[2]}`);
  }


  if(date[0] === today[1] && date[1] === today[2]) //mail sent/recieved today
  {
    return (`${date[3]} ${date[4]}`); //return only time
  }

  return(`${date[0]} ${date[1]}`); // else return month and day only

}
function mail_list(is_read, sender, subject, date,i){

  is_read = is_read ? "read" : "unread";

  document.querySelector('#maillist').innerHTML += `
    <li class=${is_read}>
      <div class="col col-1"><span class="dot"></span>
        <div class="checkbox-wrapper">
          <input type="checkbox" id="chk${i}">
          <label for="chk${i}" class="togge"></label>
        </div>
        <p class="title">${sender}</p><span class="star-toggle glyphicon glyphicon-star-empty"></span>
      </div>
      <div class="col col-2">
        <div class="subject">${subject}<span class="teaser"></span></div>
        <div class="date">${date}</div>
      </div>
    </li>`;

}


function send_email(event) {

  // Modifies the default beheavor so it doesn't reload the page after submitting.
  event.preventDefault();

  // Get the required fields.
  const recipients = document.querySelector("#compose-recipients").value;
  const subject = document.querySelector("#compose-subject").value;
  const body = document.querySelector("#compose-body").value;

  // Send the data to the server.
  fetch('/emails', {
    method: 'POST',
    body: JSON.stringify({
        recipients: recipients,
        subject: subject,
        body:  body
    })
  })
  .then(response => response.json())
  .then(result => {
      // Print result
      console.log(result);
  });

}

