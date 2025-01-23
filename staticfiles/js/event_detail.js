//Comment Form Submission Code
commentForm.addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = new FormData(this);
    fetch(this.action, {
        method: 'POST',
        body: formData,
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': '{{ csrf_token }}'
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            const commentList = document.getElementById('comment-list');
            const newComment = createCommentElement(data.comment);
            commentList.insertBefore(newComment, commentList.firstChild);
            document.getElementById('comment-count').innerText = data.comment_count;
            this.reset();
        }
    });
});


//Create Comment Function 
function createCommentElement(comment) {
    const newComment = document.createElement('li');
    newComment.classList.add('list-group-item');
    newComment.id = `comment-${comment.pk}`;
    newComment.innerHTML = `
        <p>${comment.content}</p>
        <small>By ${comment.user} on ${comment.created_at}</small>
        <div class="mt-2">
            <a href="/comments/${comment.pk}/update/" class="btn btn-warning btn-sm edit-comment">Edit</a>
            <a href="/comments/${comment.pk}/delete/" class="btn btn-danger btn-sm delete-comment">Delete</a>
        </div>
    `;
    return newComment;
}

//Event delegation for edit and delete buttons
document.addEventListener('click', function(event) {
    if (event.target.classList.contains('edit-comment')) {
        event.preventDefault();
        const commentId = event.target.closest('li').id.split('-')[1];
        const commentContent = event.target.closest('li').querySelector('p').textContent;
        showEditForm(commentId, commentContent);
    } else if (event.target.classList.contains('delete-comment')) {
        event.preventDefault();
        const commentId = event.target.closest('li').id.split('-')[1];
        deleteComment(commentId);
    }
});

//function for editing and deleting comments
function showEditForm(commentId, content) {
    const commentElement = document.getElementById(`comment-${commentId}`);
    const form = document.createElement('form');
    form.innerHTML = `
        <textarea class="form-control" name="content">${content}</textarea>
        <button type="submit" class="btn btn-primary btn-sm mt-2">Update</button>
        <button type="button" class="btn btn-secondary btn-sm mt-2 cancel-edit">Cancel</button>
    `;
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        updateComment(commentId, this);
    });
    commentElement.appendChild(form);
    commentElement.querySelector('.edit-comment').style.display = 'none';
}

function updateComment(commentId, form) {
    const formData = new FormData(form);
    fetch(`/comments/${commentId}/update/`, {
        method: 'POST',
        body: formData,
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': '{{ csrf_token }}'
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            const commentElement = document.getElementById(`comment-${commentId}`);
            commentElement.querySelector('p').textContent = data.comment.content;
            commentElement.querySelector('small').textContent = `By ${data.comment.user} on ${data.comment.created_at}`;
            form.remove();
            commentElement.querySelector('.edit-comment').style.display = 'inline-block';
        }
    });
}

function deleteComment(commentId) {
    if (confirm('Are you sure you want to delete this comment?')) {
        fetch(`/comments/${commentId}/delete/`, {
            method: 'POST',
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': '{{ csrf_token }}'
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                const commentElement = document.getElementById(`comment-${commentId}`);
                commentElement.remove();
                document.getElementById('comment-count').innerText = data.comment_count;
            }
        });
    }
}
