const API_URL = "http://127.0.0.1:5000/api/tareas";

async function cargarTareas() {
  const res = await fetch(API_URL);
  const tareas = await res.json();
  const lista = document.getElementById("listaTareas");
  lista.innerHTML = "";
  tareas.forEach(t => {
    const li = document.createElement("li");
    li.className = list-group-item d-flex justify-content-between align-items-center ${t.estado};
    li.textContent = ${t.titulo} - ${t.estado};

    const btns = document.createElement("div");

    const btnCheck = document.createElement("button");
    btnCheck.className = "btn btn-sm btn-primary me-2";
    btnCheck.textContent = "✔";
    btnCheck.onclick = async () => {
      await fetch(${API_URL}/${t.id}, {
        method: "PUT",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ estado: "completada" })
      });
      cargarTareas();
    };

    const btnDelete = document.createElement("button");
    btnDelete.className = "btn btn-sm btn-danger";
    btnDelete.textContent = "🗑";
    btnDelete.onclick = async () => {
      await fetch(${API_URL}/${t.id}, { method: "DELETE" });
      cargarTareas();
    };

    btns.appendChild(btnCheck);
    btns.appendChild(btnDelete);
    li.appendChild(btns);
    lista.appendChild(li);
  });
}

document.getElementById("tareaForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const titulo = document.getElementById("titulo").value;
  const descripcion = document.getElementById("descripcion").value;
  await fetch(API_URL, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ titulo, descripcion, usuario_id: 1 })
  });
  e.target.reset();
  cargarTareas();
});

cargarTareas();