async function send(){
  const file = document.getElementById('file').files[0];
  if(!file) return;

  const data = new FormData();
  data.append('file', file);

  const res = await fetch('/api/process', { method:'POST', body:data });
  const json = await res.json();

  document.getElementById('out').textContent =
    JSON.stringify(json, null, 2);
}
