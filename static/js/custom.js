// static/js/custom.js

function confirmDelete(url) {
  Swal.fire({
    title: 'Are you sure?',
    text: "You won't be able to revert this!",
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Yes, delete it!'
  }).then((result) => {
    if (result.isConfirmed) {
      window.location.href = url;
    }
  });
}

function confirmUpdate(url) {
  Swal.fire({
    title: 'Update this item?',
    icon: 'question',
    showCancelButton: true,
    confirmButtonText: 'Yes, update it!'
  }).then((result) => {
    if (result.isConfirmed) {
      window.location.href = url;
    }
  });
}

function likeItem(url) {
  fetch(url, {
    method: 'POST',
    headers: {
      'X-CSRFToken': getCookie('csrftoken')
    }
  })
  .then(response => response.json())
  .then(data => {
    Swal.fire({
      title: 'Liked!',
      icon: 'success',
      timer: 1500,
      showConfirmButton: false
    });
  });
}

function addComment(url) {
  Swal.fire({
    title: 'Add a comment',
    input: 'textarea',
    inputAttributes: {
      autocapitalize: 'off'
    },
    showCancelButton: true,
    confirmButtonText: 'Submit',
    showLoaderOnConfirm: true,
    preConfirm: (comment) => {
      return fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({comment: comment})
      })
      .then(response => response.json())
    },
    allowOutsideClick: () => !Swal.isLoading()
  }).then((result) => {
    if (result.isConfirmed) {
      Swal.fire({
        title: 'Comment added!',
        icon: 'success'
      });
    }
  });
}

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

//fuction to display contact us message
document.addEventListener('DOMContentLoaded', function() {
  var toastElList = [].slice.call(document.querySelectorAll('.toast'));
  var toastList = toastElList.map(function(toastEl) {
      return new bootstrap.Toast(toastEl, {
          autohide: true,
          delay: 5000
      }).show();
  });
});
