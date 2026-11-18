# INF1103 - Lab 9: Design Patterns and Error Handling

A standalone Inventory Management System example continuing Lab 8's Product,
Supplier, Inventory, Order and OrderLine design. Files are split **one class per
file**. Your own Lab 8 source code was not supplied, so this is a complete,
runnable reference implementation rather than a patch to that exact repository.

## Included deliverables

- Python files: Product, PhysicalProduct, DigitalProduct, Supplier, Inventory,
  OrderLine, Order, abstract DiscountStrategy, NoDiscount, PercentageDiscount,
  BulkDiscount, StudentDiscount, ProductFactory, CSV loader and input helper.
- `products.csv` with exactly the example rows from Section 5.2.
- `tests/` with automated validation, design-pattern, CSV and input tests.
- `Predict_First_Notes.docx` with all eight Predict First prompts, predicted
  outcomes, observed outcomes and changes, plus the Section 1.5 diagnosis.
- `diagrams/Lab09_UML.png`, `.svg`, and editable `.dot` Graphviz source.
- Git/Docker workflow instructions and locally generated evidence in `evidence/`.

## Run locally (Windows PowerShell)

```powershell
py -m pip install -r requirements.txt
py main.py
py main.py --interactive
py -m pytest -q
```

The sample CSV loads **3** valid products and skips two bad rows, reporting the
reasons. The 250.00 order prints 230.00 (bulk), 225.00 (10% off), then 237.50
(student 5% off).

## Docker

From the directory containing Dockerfile:

```powershell
docker build -t inf1103-lab09 .
docker run --rm inf1103-lab09
docker run --rm inf1103-lab09 python -m pytest -q
```

Optional Compose:

```powershell
docker compose up --build
docker compose run --rm inventory python -m pytest -q
```

## Git workflow

```powershell
git status
git add .
git commit -m "Complete Lab 9 strategy factory validation and tests"
git push origin main
git log -5 --oneline
```

If your branch isn't `main`, replace it with your actual branch. Commit/push
from **your own existing GitHub Lab 8 project** if that is the repository your
teacher requires. Do not commit an entire downloaded ZIP on top of your
original code without reconciling any constructor differences.

## Design decisions

- **Strategy**: `Order` delegates to `DiscountStrategy.apply()` and never
  branches on discount type. `StudentDiscount` demonstrates extension without
  modifying `Order`.
- **Factory**: the production program only instantiates concrete products in
  `ProductFactory.create()`. Adding a new product type changes that central
  factory, a deliberate small-system OCP tradeoff.
- **Validation**: `Product` validates price and stock; `OrderLine` validates
  quantity. Both physical and digital products obey the base class invariants.
- **Exception handling**: CSV loader uses `except FileNotFoundError`, `else`,
  `finally`, plus a per-row `except ValueError`. Input helper retries bad input.
- **UML**: Order-to-Strategy is a shared association (`1` strategy per order;
  `0..*` orders may refer to the same strategy object). The factory's dashed
  dependency targets Product and is labelled «creates».

## Screenshot requirement: action still needed on your PC

The PDF explicitly requests a **screenshot of your own Git and Docker
workflow**. We can provide commands and locally executed Git output here, but
cannot capture your Windows terminal/GitHub push or a Docker run on your machine.
Docker is not installed in this generation environment, so no Docker success
screenshot is invented. See `evidence/SCREENSHOT_INSTRUCTIONS.md` and replace
local example evidence with genuine screenshots from your own workflow.

## Final submission checklist

- [x] Eight Predict First responses in Word document.
- [x] Python source, standalone runnable demo, tests, CSV and Dockerfile.
- [x] Updated UML diagram with Strategy, Factory and relationships.
- [x] Automated tests executed locally using pytest.
- [ ] Add screenshots from your Git push and Docker commands on your PC.
- [ ] If instructed, merge into your original Lab 8 GitHub project and push.

The Section 8 reflection is optional; brief reflection notes are included in
the Word file as a study aid.
