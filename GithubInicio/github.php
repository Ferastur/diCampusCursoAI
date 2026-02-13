<?php
// --- LÓGICA DEL CONTADOR DE VISITAS ---
$archivo_contador = "contador.txt";

// Si el archivo no existe, lo creamos con el valor 0
if (!file_exists($archivo_contador)) {
    file_put_contents($archivo_contador, "0");
}

// Leemos el valor actual, lo incrementamos y guardamos
$visitas = (int)file_get_contents($archivo_contador);
$visitas++;
file_put_contents($archivo_contador, $visitas);
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GitHub Pro Guide - Documentación Integral</title>
    
    <!-- Librerías de Visualización -->
    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">

    <style>
        :root {
            --gh-dark: #0d1117;
            --gh-blue: #0969da;
            --gh-green: #1f883d;
            --sidebar-bg: #f6f8fa;
            --border-color: #d0d7de;
            --text-primary: #1f2328;
            --text-secondary: #636c76;
            --code-bg: #f6f8fa;
        }

        * { box-sizing: border-box; }
        body {
            font-family: 'Inter', sans-serif;
            margin: 0;
            display: flex;
            color: var(--text-primary);
            background-color: #ffffff;
            scroll-behavior: smooth;
        }

        /* --- BARRA LATERAL --- */
        aside {
            width: 300px;
            height: 100vh;
            background: var(--sidebar-bg);
            border-right: 1px solid var(--border-color);
            position: fixed;
            padding: 2rem 1.5rem;
            overflow-y: auto;
            z-index: 100;
        }

        .brand {
            font-size: 1.5rem;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 2.5rem;
            color: var(--gh-dark);
        }

        .nav-section { margin-bottom: 2rem; }
        .nav-section h4 { 
            font-size: 0.75rem; 
            text-transform: uppercase; 
            color: var(--text-secondary);
            letter-spacing: 1px;
            margin-bottom: 10px;
        }

        .nav-link {
            display: block;
            padding: 8px 12px;
            color: var(--text-primary);
            text-decoration: none;
            font-size: 0.95rem;
            border-radius: 6px;
            transition: 0.2s;
        }

        .nav-link:hover { background: #eef1f4; color: var(--gh-blue); }

        /* --- CONTENIDO --- */
        main {
            margin-left: 300px;
            padding: 4rem 10%;
            width: 100%;
            max-width: 1200px;
        }

        .hero {
            background: var(--gh-dark);
            color: white;
            padding: 3rem;
            border-radius: 12px;
            margin-bottom: 4rem;
            position: relative;
        }

        .visitor-counter {
            position: absolute;
            top: 20px;
            right: 20px;
            background: rgba(255,255,255,0.1);
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.8rem;
            font-family: 'Fira Code', monospace;
        }

        h1 { font-size: 2.8rem; margin: 0; }
        h2 { font-size: 2rem; border-bottom: 1px solid var(--border-color); padding-bottom: 10px; margin-top: 4rem; }
        h3 { color: var(--gh-blue); margin-top: 2rem; }

        .diagram-container {
            background: white;
            border: 1px solid var(--border-color);
            border-radius: 10px;
            padding: 20px;
            margin: 25px 0;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        }

        .alert {
            padding: 1rem 1.5rem;
            border-radius: 8px;
            margin: 20px 0;
            border-left: 5px solid;
        }
        .alert-info { background: #f0f7ff; border-color: var(--gh-blue); }
        .alert-success { background: #dafbe1; border-color: var(--gh-green); }

        code { font-family: 'Fira Code', monospace; background: var(--code-bg); padding: 3px 6px; border-radius: 4px; }
        
        pre {
            background: #1e1e1e;
            color: #d4d4d4;
            padding: 1.5rem;
            border-radius: 8px;
            overflow-x: auto;
        }

        .step-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin: 2rem 0;
        }

        .step-card {
            border: 1px solid var(--border-color);
            padding: 1.5rem;
            border-radius: 8px;
            background: #fff;
        }

        footer {
            margin-top: 6rem;
            padding: 2rem;
            border-top: 1px solid var(--border-color);
            text-align: center;
            color: var(--text-secondary);
        }

        @media (max-width: 900px) {
            aside { display: none; }
            main { margin-left: 0; padding: 2rem; }
        }
    </style>
</head>
<body>

<aside>
    <div class="brand"><i class="fab fa-github"></i> GitHub Wiki</div>
    
    <div class="nav-section">
        <h4>Fundamentos</h4>
        <a href="#conceptos" class="nav-link"><i class="fas fa-book"></i> ¿Qué es Git/GitHub?</a>
        <a href="#arquitectura" class="nav-link"><i class="fas fa-sitemap"></i> Arquitectura</a>
    </div>

    <div class="nav-section">
        <h4>Instalación</h4>
        <a href="#desktop" class="nav-link"><i class="fas fa-desktop"></i> GitHub Desktop</a>
        <a href="#login" class="nav-link"><i class="fas fa-key"></i> Autenticación</a>
    </div>

    <div class="nav-section">
        <h4>Operaciones</h4>
        <a href="#crear" class="nav-link"><i class="fas fa-plus-circle"></i> Crear Repositorios</a>
        <a href="#workflow" class="nav-link"><i class="fas fa-sync"></i> El Flujo (Commit/Push)</a>
        <a href="#ramas" class="nav-link"><i class="fas fa-code-branch"></i> Ramas y Colaboración</a>
    </div>
</aside>

<main>
    <div class="hero">
        <div class="visitor-counter">
            <i class="fas fa-eye"></i> Visitas: <?php echo $visitas; ?>
        </div>
        <h1>Guía Maestra de GitHub</h1>
        <p>Aprende el estándar de la industria para el desarrollo colaborativo de software.</p>
    </div>

    <!-- SECCION 1 -->
    <section id="conceptos">
        <h2>1. Conceptos Fundamentales</h2>
        <p>No son lo mismo. Es vital entender la diferencia técnica:</p>
        <div class="step-grid">
            <div class="step-card">
                <h3>Git (El Motor)</h3>
                <p>Es un software de <strong>Control de Versiones</strong> distribuido. Se ejecuta localmente en tu computadora. Rastrea cambios línea por línea.</p>
            </div>
            <div class="step-card">
                <h3>GitHub (La Plataforma)</h3>
                <p>Es un servicio en la nube que aloja repositorios Git. Facilita la colaboración, gestión de proyectos y el despliegue.</p>
            </div>
        </div>
    </section>

    <!-- SECCION 2: ARQUITECTURA -->
    <section id="arquitectura">
        <h2>2. Arquitectura de Datos de Git</h2>
        <p>El código viaja a través de 4 estados principales antes de ser público:</p>
        
        <div class="diagram-container">
            <div class="mermaid">
                graph LR
                A[Working Dir] -- git add --> B[Staging Area]
                B -- git commit --> C[Local Repo]
                C -- git push --> D((Remote GitHub))
                style D fill:#0969da,color:#fff
            </div>
        </div>

        <div class="alert alert-info">
            <strong>💡 Tip:</strong> El <em>Staging Area</em> es como una cesta de compra; pones los cambios que quieres subir antes de confirmar la "compra" (Commit).
        </div>
    </section>

    <!-- SECCION 3: DESKTOP -->
    <section id="desktop">
        <h2>3. Instalación de GitHub Desktop</h2>
        <p>GitHub Desktop simplifica Git eliminando la necesidad de comandos en consola para el 90% de las tareas diarias.</p>
        
        <div class="step-grid">
            <div class="step-card">
                <i class="fas fa-1 fa-2x"></i>
                <p>Descarga desde <a href="https://desktop.github.com/">desktop.github.com</a></p>
            </div>
            <div class="step-card">
                <i class="fas fa-2 fa-2x"></i>
                <p>Instala y abre la aplicación. Inicia sesión con tus credenciales de GitHub.</p>
            </div>
            <div class="step-card">
                <i class="fas fa-3 fa-2x"></i>
                <p>Configura tu <strong>Nombre y Email</strong>. Esto es vital para que tus commits tengan autoría.</p>
            </div>
        </div>
    </section>

    <!-- SECCION 4: CREAR REPOSITORIO -->
    <section id="crear">
        <h2>4. Crear un Repositorio (Paso a Paso)</h2>
        <p>Sigue esta receta para empezar un proyecto profesional:</p>
        
        <ol>
            <li>En GitHub Desktop: <code>File -> New Repository</code>.</li>
            <li><strong>Nombre:</strong> Usa nombres descriptivos (ej: <code>sistema-ventas-php</code>).</li>
            <li><strong>Local Path:</strong> Elige una carpeta de fácil acceso.</li>
            <li><strong>Git Ignore:</strong> Elige el lenguaje de tu proyecto (ej: PHP). Esto evita subir archivos basura.</li>
            <li><strong>License:</strong> Selecciona <em>MIT License</em> para proyectos abiertos.</li>
        </ol>

        <div class="alert alert-success">
            <strong>Importante:</strong> Tras crearlo, pulsa el botón <strong>"Publish Repository"</strong>. Si no lo haces, el código solo existirá en tu PC.
        </div>
    </section>

    <!-- SECCION 5: WORKFLOW -->
    <section id="workflow">
        <h2>5. El Ciclo de Trabajo Diario</h2>
        <p>Cada vez que trabajes, repetirás este ciclo sagrado:</p>
        
        <div class="diagram-container">
            <div class="mermaid">
                sequenceDiagram
                participant PC as Tu Computadora
                participant GH as Servidor GitHub
                Note over PC: 1. Realizas cambios en el código
                PC->>PC: 2. Commit (Guardar foto local)
                PC->>GH: 3. Push (Subir a la nube)
                GH->>PC: 4. Pull (Bajar cambios de otros)
            </div>
        </div>
    </section>

    <!-- SECCION 6: RAMAS -->
    <section id="ramas">
        <h2>6. Ramas (Branches) y Pull Requests</h2>
        <p>En el mundo profesional, nunca se toca la rama <code>main</code> directamente.</p>
        
        <div class="diagram-container">
            <div class="mermaid">
                gitGraph
                commit
                branch feature-nueva-funcionalidad
                checkout feature-nueva-funcionalidad
                commit
                commit
                checkout main
                merge feature-nueva-funcionalidad
            </div>
        </div>

        <h3>¿Qué es un Pull Request (PR)?</h3>
        <p>Cuando terminas una rama, pides permiso para unirla a la principal. Es el lugar donde se revisa el código:</p>
        <ul>
            <li><strong>Review:</strong> Otros ven errores o sugieren mejoras.</li>
            <li><strong>CI/CD:</strong> Se pasan pruebas automáticas.</li>
            <li><strong>Merge:</strong> Se aprueba y el código se une al proyecto oficial.</li>
        </ul>
    </section>

    <section>
        <h2>7. Markdown: El lenguaje de la documentación</h2>
        <p>Tu archivo <code>README.md</code> debe verse bien. Aquí tienes una chuleta rápida:</p>
        <pre>
# Título H1
## Subtítulo H2
**Texto en Negrita**
[Enlace a mi web](https://google.com)
* Elemento de lista 1
* Elemento de lista 2
        </pre>
    </section>

    <footer>
        <p>&copy; <?php echo date("Y"); ?> - Manual del Desarrollador GitHub Pro</p>
        <p><small>Este sitio ha sido visitado <?php echo $visitas; ?> veces.</small></p>
    </footer>
</main>

<script>
    // Inicialización de Mermaid con tema profesional
    mermaid.initialize({ 
        startOnLoad: true,
        theme: 'neutral',
        fontFamily: 'Inter'
    });
</script>

</body>
</html>