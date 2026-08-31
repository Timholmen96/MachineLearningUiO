# GitHub Pipeline

## In practice

The original repository is configured as `upstream`:

```text
EducationalMaterialUiO/MachineLearningUiO
```

Your fork is configured as `origin`:

```text
Timholmen96/MachineLearningUiO
```

0. Git status
1. git switch secunda
2. git add .
3. git commit -m "Week x work"

4. Update local `main` from the original repository:

   ```bash
   git switch main
   git pull upstream main
   ```

5. Merge the updates into your working branch, `secunda`:

   ```bash
   git switch secunda
   git merge main
   ```

6. Push your work to the `secunda` branch on your fork:

   ```bash
   git push origin secunda
   ```

You work and write exercises on `secunda`. The original repository is only used as a source of updates. You do not need to push `main` to your fork.

```mermaid
flowchart LR
    A[EducationalMaterialUiO original repository] -->|fetch upstream/main| B[Local main]
    B -->|merge| C[Local secunda]
    C -->|push origin secunda| D[Your GitHub fork]
```

The GitHub Pages workflow runs when `main` receives a push. Pushing `secunda` updates your fork's working branch but does not trigger that deployment workflow.
