<?php
// Lógica del contador de visitas
$archivo = "visitas_powerpoint.txt";
if (!file_exists($archivo)) { file_put_contents($archivo, "0"); }
$contador = (int)file_get_contents($archivo) + 1;
file_put_contents($archivo, $contador);

// Definición de contenido de las 10 Diapositivas
$slides = [
    [
        "title" => "El Universo GitHub",
        "subtitle" => "Mucho más que un simple almacén de código",
        "content" => "GitHub es la red social y plataforma de colaboración más grande para desarrolladores. Permite alojar proyectos utilizando el sistema de control de versiones Git.",
        "type" => "intro",
        "visual" => "<i class='fab fa-github fa-10x' style='color: #fff; filter: drop-shadow(0 0 20px #6e5494);'></i>"
    ],
    [
        "title" => "Git vs GitHub: La Dualidad",
        "subtitle" => "Entendiendo la herramienta frente al servicio",
        "content" => "<b>Git</b> es el motor local que rastrea cambios. <b>GitHub</b> es el garaje global en la nube donde guardas y compartes esos motores.",
        "type" => "diagram",
        "visual" => "graph LR
            A[Tu PC con Git] -->|Push| B((GitHub Cloud))
            B -->|Pull| C[Equipo de Trabajo]
            style B fill:#238636,stroke:#fff,color:#fff"
    ],
    [
        "title" => "Instalación: GitHub Desktop",
        "subtitle" => "La interfaz visual definitiva",
        "content" => "Evita la terminal al principio. GitHub Desktop te permite gestionar repositorios con botones intuitivos. <br><br> 1. Descarga en desktop.github.com <br> 2. Loguea tu cuenta <br> 3. Configura tu Git (Nombre/Email).",
        "type" => "content",
        "visual" => "<div class='mockup'> <i class='fas fa-desktop'></i> Descargar -> Instalar -> Sincronizar </div>"
    ],
    [
        "title" => "Anatomía de un Repositorio",
        "subtitle" => "Los pilares de un proyecto profesional",
        "content" => "Un repo no son solo archivos, es una estructura: <br> • <b>README.md:</b> La cara del proyecto. <br> • <b>.gitignore:</b> Qué archivos ignorar (node_modules, .env). <br> • <b>License:</b> Reglas de uso legal.",
        "type" => "content",
        "visual" => "<div class='file-grid'><i class='fas fa-file-code'></i> <i class='fas fa-book-open'></i> <i class='fas fa-shield-halved'></i></div>"
    ],
    [
        "title" => "El Ciclo de Vida del Código",
        "subtitle" => "Add -> Commit -> Push",
        "content" => "El flujo diario se resume en tres pasos críticos para asegurar que tu trabajo no se pierda y esté siempre disponible en la nube.",
        "type" => "diagram",
        "visual" => "sequenceDiagram
            participant PC as Workspace
            participant ST as Staging Area
            participant LC as Local Repo
            participant GH as GitHub
            PC->>ST: git add (Preparar)
            ST->>LC: git commit (Guardar)
            LC->>GH: git push (Subir)"
    ],
    [
        "title" => "Estrategia de Ramas",
        "subtitle" => "Trabaja en paralelo sin romper nada",
        "content" => "Las <b>Branches</b> permiten crear funciones nuevas sin afectar la rama principal (main). Es la base del desarrollo profesional moderno.",
        "type" => "diagram",
        "visual" => "gitGraph
            commit
            branch feature-nueva
            checkout feature-nueva
            commit
            commit
            checkout main
            merge feature-nueva"
    ],
    [
        "title" => "Pull Requests (PR)",
        "subtitle" => "El corazón de la revisión por pares",
        "content" => "Un PR es una solicitud para fusionar tus cambios. Aquí ocurre la magia: <br> • Revisión de código. <br> • Comentarios de mejora. <br> • Aprobación final antes del Merge.",
        "type" => "content",
        "visual" => "<div class='badge-pro'>REVISIÓN -> APROBACIÓN -> FUSIÓN</div>"
    ],
    [
        "title" => "Conflictos de Merge",
        "subtitle" => "Cuando dos personas tocan lo mismo",
        "content" => "Si tú y un colega editáis la misma línea, Git se detendrá. GitHub Desktop te mostrará visualmente ambas opciones para que elijas cuál conservar.",
        "type" => "content",
        "visual" => "<div class='warning-ui'><i class='fas fa-triangle-exclamation'></i> ¡Conflicto detectado!</div>"
    ],
    [
        "title" => "GitHub Social",
        "subtitle" => "Issues, Stars y Forks",
        "content" => "• <b>Issues:</b> Lista de tareas y bugs. <br> • <b>Stars:</b> Marcadores/Me gusta. <br> • <b>Forks:</b> Copiar un proyecto ajeno para mejorarlo tú mismo.",
        "type" => "content",
        "visual" => "<div class='social-icons'><i class='fas fa-star'></i> <i class='fas fa-code-fork'></i> <i class='fas fa-circle-dot'></i></div>"
    ],
    [
        "title" => "¡Felicidades, Git Master!",
        "subtitle" => "Próximos pasos en tu carrera",
        "content" => "Ya conoces los fundamentos. Ahora crea tu primer repositorio, sube tu código y empieza a colaborar con el mundo. <br><br> <b>Recuerda: Pull antes de empezar, Push al terminar.</b>",
        "type" => "intro",
        "visual" => "<i class='fas fa-award fa-8x' style='color: #ffd700;'></i>"
    ]
];
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>GitHub Masterclass Presentation</title>
    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-gradient: linear-gradient(135deg, #0d1117 0%, #161b22 100%);
            --accent: #238636;
            --blue: #2f81f7;
            --glass: rgba(255, 255, 255, 0.05);
            --border: rgba(255, 255, 255, 0.1);
        }

        body {
            margin: 0; padding: 0;
            background: var(--bg-gradient);
            color: #fff;
            font-family: 'Poppins', sans-serif;
            overflow: hidden;
            height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }

        /* --- ESCENARIO DE LA DIAPOSITIVA --- */
        .stage {
            width: 90vw;
            height: 80vh;
            max-width: 1200px;
            max-height: 675px; /* Proporción 16:9 */
            background: var(--glass);
            backdrop-filter: blur(10px);
            border: 1px solid var(--border);
            border-radius: 20px;
            display: flex;
            position: relative;
            box-shadow: 0 25px 50px rgba(0,0,0,0.5);
        }

        .slide {
            display: none;
            width: 100%;
            height: 100%;
            padding: 60px;
            box-sizing: border-box;
            grid-template-columns: 1fr 1fr;
            gap: 40px;
            align-items: center;
            animation: slideIn 0.6s cubic-bezier(0.23, 1, 0.32, 1);
        }

        .slide.active { display: grid; }

        @keyframes slideIn {
            from { opacity: 0; transform: translateX(50px); }
            to { opacity: 1; transform: translateX(0); }
        }

        /* --- TEXTOS --- */
        .content-side h1 { font-size: 3.5rem; margin: 0; line-height: 1.1; background: linear-gradient(to right, #fff, #8b949e); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .content-side h3 { color: var(--blue); font-weight: 400; margin: 10px 0 30px 0; font-size: 1.5rem; }
        .content-side p { font-size: 1.2rem; color: #8b949e; line-height: 1.6; }

        /* --- VISUALES --- */
        .visual-side {
            background: rgba(0,0,0,0.2);
            border-radius: 15px;
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
            border: 1px solid var(--border);
        }

        .mermaid { background: white !important; width: 90%; padding: 20px; border-radius: 10px; }

        /* --- UI DE NAVEGACIÓN --- */
        .controls {
            position: fixed;
            bottom: 30px;
            display: flex;
            gap: 15px;
            align-items: center;
            z-index: 100;
        }

        .nav-btn {
            background: var(--glass);
            border: 1px solid var(--border);
            color: white;
            padding: 15px 25px;
            border-radius: 12px;
            cursor: pointer;
            transition: 0.3s;
            font-weight: bold;
        }

        .nav-btn:hover { background: var(--blue); border-color: var(--blue); }
        .nav-btn:disabled { opacity: 0.3; cursor: not-allowed; }

        .progress-bar {
            position: fixed;
            top: 0; left: 0; height: 5px;
            background: var(--blue);
            box-shadow: 0 0 10px var(--blue);
            transition: 0.4s cubic-bezier(0.23, 1, 0.32, 1);
        }

        .visitas {
            position: fixed;
            top: 20px; right: 30px;
            font-size: 0.8rem;
            color: #8b949e;
            background: var(--glass);
            padding: 5px 15px;
            border-radius: 20px;
        }

        /* --- DECORACIONES ESPECIALES --- */
        .file-grid i { font-size: 5rem; margin: 0 15px; color: var(--blue); opacity: 0.8; }
        .badge-pro { background: var(--accent); padding: 20px; border-radius: 10px; font-weight: bold; font-size: 1.5rem; letter-spacing: 2px; }
        .warning-ui { color: #f85149; font-size: 2rem; font-weight: bold; text-align: center; }
        .social-icons i { font-size: 4rem; margin: 0 20px; color: #d1d5da; }

        @media (max-width: 1000px) {
            .slide { grid-template-columns: 1fr; padding: 30px; text-align: center; }
            .visual-side { display: none; }
        }
    </style>
</head>
<body>

    <div class="progress-bar" id="progress"></div>
    <div class="visitas">SESIÓN DE APRENDIZAJE • VISITAS: <?php echo $contador; ?></div>

    <div class="stage">
        <?php foreach ($slides as $i => $s): ?>
            <div class="slide <?php echo $i === 0 ? 'active' : ''; ?>" id="slide-<?php echo $i; ?>">
                <div class="content-side">
                    <h1><?php echo $s['title']; ?></h1>
                    <h3><?php echo $s['subtitle']; ?></h3>
                    <p><?php echo $s['content']; ?></p>
                </div>
                <div class="visual-side">
                    <?php if ($s['type'] === 'diagram'): ?>
                        <div class="mermaid"><?php echo $s['visual']; ?></div>
                    <?php else: ?>
                        <?php echo $s['visual']; ?>
                    <?php endif; ?>
                </div>
            </div>
        <?php endforeach; ?>
    </div>

    <div class="controls">
        <button class="nav-btn" onclick="move(-1)" id="btnPrev"><i class="fas fa-chevron-left"></i></button>
        <span id="label">1 / 10</span>
        <button class="nav-btn" onclick="move(1)" id="btnNext"><i class="fas fa-chevron-right"></i></button>
    </div>

    <script>
        let current = 0;
        const total = <?php echo count($slides); ?>;

        function move(dir) {
            current += dir;
            if (current < 0) current = 0;
            if (current >= total) current = total - 1;
            update();
        }

        function update() {
            // Slides
            document.querySelectorAll('.slide').forEach((s, i) => {
                s.classList.toggle('active', i === current);
            });

            // UI
            document.getElementById('label').innerText = `${current + 1} / ${total}`;
            document.getElementById('btnPrev').disabled = current === 0;
            document.getElementById('btnNext').disabled = current === total - 1;
            
            // Progress
            document.getElementById('progress').style.width = ((current + 1) / total * 100) + '%';

            // Re-render Mermaid (Crucial para que no de error al cambiar de slide)
            mermaid.init(undefined, ".mermaid");
        }

        // Teclado
        document.addEventListener('keydown', (e) => {
            if (e.key === "ArrowRight" || e.key === "Enter") move(1);
            if (e.key === "ArrowLeft") move(-1);
        });

        // Mermaid Config
        mermaid.initialize({ 
            startOnLoad: true, 
            theme: 'neutral',
            securityLevel: 'loose',
            gitGraph: { mainBranchName: 'main' }
        });
    </script>
</body>
</html>