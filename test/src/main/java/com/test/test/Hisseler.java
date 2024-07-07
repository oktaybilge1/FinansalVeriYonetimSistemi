package com.test.test;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;

@Entity
public class Hisseler {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String hisse;
    private String son_deger;
    private String degisim_yuzde;
    private String hacim;
    private String saat;

    // Getter ve Setter metotları
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getHisse() {
        return hisse;
    }

    public void setHisse(String hisse) {
        this.hisse = hisse;
    }

    public String getSon_deger() {
        return son_deger;
    }

    public void setSon_deger(String son_deger) {
        this.son_deger = son_deger;
    }

    public String getDegisim_yuzde() {
        return degisim_yuzde;
    }

    public void setDegisim_yuzde(String degisim_yuzde) {
        this.degisim_yuzde = degisim_yuzde;
    }

    public String getHacim() {
        return hacim;
    }

    public void setHacim(String hacim) {
        this.hacim = hacim;
    }

    public String getSaat() {
        return saat;
    }

    public void setSaat(String saat) {
        this.saat = saat;
    }
}
