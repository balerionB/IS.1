/*
==========================================
Attachment Module
==========================================
*/

document.addEventListener("DOMContentLoaded", () => {

    const input = document.getElementById("attachmentInput");

    if(input){

        input.addEventListener(

            "change",

            uploadFiles

        );

    }

});

async function uploadFiles(event){

    const files = event.target.files;

    if(files.length===0){

        return;

    }

    for(const file of files){

        await uploadSingleFile(file);

    }

}
async function uploadSingleFile(file){

    const formData = new FormData();

    formData.append("file",file);

    const requestId=document.body.dataset.requestId;

    const response=await fetch(

        `/attachments/upload/${requestId}`,

        {

            method:"POST",

            body:formData

        }

    );

    if(response.ok){

        loadAttachments();

    }

}
async function loadAttachments(){

    const requestId=document.body.dataset.requestId;

    const response=await fetch(

        `/attachments/list/${requestId}`

    );

    const attachments=

        await response.json();

    renderAttachments(

        attachments

    );

}
document.addEventListener("DOMContentLoaded", () => {
    const input = document.getElementById("attachmentInput");

    if (input) {
        input.addEventListener("change", uploadFiles);
    }

    loadAttachments();
});
function renderAttachments(attachments){

    const list=

        document.getElementById("attachmentList");

    if(attachments.length===0){

        list.innerHTML=`

        <div class="text-muted">

            No attachments uploaded.

        </div>

        `;

        return;

    }

    let html="";

    attachments.forEach(file=>{

        html+=`

<div class="attachment-item">

<div>

<div class="attachment-name">

${file.file_name}

</div>

<small>

${file.content_type}

</small>

</div>

<div class="attachment-actions">

<button

class="btn btn-sm btn-success"

onclick="downloadAttachment(${file.id})">

Download

</button>

<button

class="btn btn-sm btn-danger"

onclick="deleteAttachment(${file.id})">

Delete

</button>

</div>

</div>

`;

    });

    list.innerHTML=html;

}
@attachments.route("/list/<int:request_id>")
@login_required
def list_files(request_id):

    attachments = Attachment.query.filter_by(

        request_id=request_id

    ).all()

    return jsonify([

        {

            "id": file.id,

            "file_name": file.file_name,

            "content_type": file.content_type,

            "size": file.file_size

        }

        for file in attachments

    ])
    document.addEventListener(

"DOMContentLoaded",

()=>{

loadAttachments();

});

const requestId = document
    .getElementById("requestPage")
    .dataset
    .requestId;
    from flask import redirect

@attachments.route("/download/<int:id>")
@login_required
def download(id):

    attachment = Attachment.query.get_or_404(id)

    url = S3Service.generate_download_url(

        attachment.s3_key

    )

    return redirect(url)

    function downloadAttachment(id){

    window.location=

        `/attachments/download/${id}`;

}
async function deleteAttachment(id){

    if(!confirm(

        "Delete this attachment?"

    )){

        return;

    }

    const response=

        await fetch(

            `/attachments/delete/${id}`,

            {

                method:"DELETE"

            }

        );

    if(response.ok){

        loadAttachments();

    }

}
function previewAttachment(id){

    window.open(

        `/attachments/preview/${id}`,

        "_blank"

    );

}